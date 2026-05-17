from __future__ import annotations
import json
import re
import time
from functools import lru_cache
from typing import Any, Dict, List, Optional

from mlflow.genai.scorers import scorer
from openai import OpenAI, RateLimitError

from rag_core.config import JUDGE_API_KEY, JUDGE_BASE_URL, JUDGE_MODEL, TRIAD_MAX_CHARS
from rag_core.deterministic_core import build_zakon_id, safe_str

_REFUSAL_MARKERS = (
    "insufficient data to verify",
    "nedostatok udajov",
    "nedostatok dat",
    "nie je mozne overit",
    "neviem",
)

_ZAKON_ID_PARTS_RE = re.compile(r"^(?P<law>\d+/\d{4})/paragraf-(?P<paragraph>\d+[a-zA-Z]?)$", re.IGNORECASE)
_SCORE_RE = re.compile(r'"score"\s*:\s*([01](?:\.\d+)?)')
_JUDGE_EXPLANATION_MAX_CHARS = 12000

_LAW_SHORT_NAMES = {
    "513/1991": "ObZ",
    "40/1964": "OZ",
}

TRIAD_JUDGE_LOG: List[Dict[str, Any]] = []

GROUNDEDNESS_SYSTEM_PROMPT = """
Posudzujes, ci je finalna odpoved vecne podlozena obsahom retrieved contextu.
Zniz skore za kazde vecne tvrdenie, ktore v contexte nema oporu.
V odovodneni jasne povedz, ktore tvrdenia odpovede su podlozene a ktore nie.
Ak je odpoved dobre podlozena, pomenuj, o ake casti contextu sa opiera.
Odovodnenie napis po slovensky, vecne a konkretne.
Vrat IBA validny JSON:
{"score": <0..1>, "explanation": "<slovenske odovodnenie>"}
Ziadne dalsie kluce.
""".strip()

SPAN_FAITHFULNESS_SYSTEM_PROMPT = """
Posudzujes metriku 2: ci text modelu pre jeden konkretny pravny predpis verne vystihuje obsah citovaneho pravneho predpisu.

Hodnotis iba vztah medzi textom modelu a textom pravneho predpisu pre ten isty paragraf.
Nevyzaduj doslovnu zhodu ani uplne rovnaku formulaciu.
Kratka parafraza alebo zhrnutie je v poriadku, ak nemenia pravny vyznam.

Pouzi iba tieto skore:
- 1.0 = text modelu je vecne podporeny pravnym predpisom a nepridava nic podstatne navyse,
- 0.5 = text modelu je iba ciastocne podporeny; jadro je spravne, ale je nepresny, prilis vseobecny alebo miestami doplna nieco, co nie je plne iste,
- 0.0 = text modelu je nepodporeny, skresluje pravny vyznam alebo pripisuje predpisu nieco, co z neho nevyplyva.

V odovodneni pis prirodzene po slovensky. Nevypisuj technicke placeholdery ani nazvy vstupnych blokov.
Namiesto toho hovori priamo o texte modelu a o texte pravneho predpisu.
Vysvetli:
- co z textu modelu je podlozene,
- co je nepresne alebo nepodlozene,
- preco si zvolil dane skore.

Vrat IBA validny JSON:
{"score": <0 | 0.5 | 1>, "explanation": "<slovenske odovodnenie>"}
Ziadne dalsie kluce.
""".strip()

STATUTE_CONTEXT_EXTRACTION_SYSTEM_PROMPT = """
Si pomocna extrakcna metoda pre pravne hodnotenie.
Dostanes full text, v ktorom je cielovy pravny predpis oznaceny pomocou ***...***.
Vrat najmensi suvisly vyrez textu, ktory sa tomuto oznacenemu predpisu skutocne venuje.
Zachovaj povodne znenie vyrezu vratane hviezdiciek.
Ak treba pre zmysel, pridaj aj bezprostredne susediacu vetu, uvadzajucu vetu alebo odrazku.
Ak sa text oznacenemu predpisu v skutocnosti nevenuje, vrat prazdny span.
Ak je v texte viac miest s tym istym predpisom, vyber to miesto, ktore najviac vecne rozvija oznaceny pravny bod.
Dovod napis po slovensky, vecne a konkretne.
Vrat IBA validny JSON:
{"span": "<vyrez alebo prazdny retazec>", "reason": "<slovenske odovodnenie>"}
Ziadne dalsie kluce.
""".strip()

SPAN_ALIGNMENT_SYSTEM_PROMPT = """
Posudzujes metriku 3: ci text modelu pre jeden konkretny pravny predpis vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

Hodnotis iba vztah medzi textom modelu a relevantnym expertne oznacenym spanom.
Nevyzaduj uplnu vycerpavajucnost.
Kratsi text modelu je v poriadku, ak zachytava spravne jadro pravneho bodu.

Pouzi iba tieto skore:
- 1.0 = text modelu je vecne v sulade s expertne oznacenym spanom,
- 0.5 = text modelu je iba ciastocne v sulade; jadro sedi, ale formulacia je nepresna, neuplna alebo mierne posunuta,
- 0.0 = text modelu je v rozpore s expertne oznacenym spanom alebo hovori o inom pravnom bode.

V odovodneni pis prirodzene po slovensky. Nevypisuj technicke placeholdery ani nazvy vstupnych blokov.
Namiesto toho hovori priamo o texte modelu a o relevantnej casti expertnej odpovede.
Vysvetli:
- v com je zhoda,
- v com je rozdiel,
- preco si zvolil dane skore.

Vrat IBA validny JSON:
{"score": <0 | 0.5 | 1>, "explanation": "<slovenske odovodnenie>"}
Ziadne dalsie kluce.
""".strip()

SPAN_FAITHFULNESS_BATCH_SYSTEM_PROMPT = """
Posudzujes metriku 2 pre viacero pravnych predpisov naraz.

Pre kazdy zaznam dostanes:
- identifikator pravneho predpisu,
- text modelu pre tento predpis,
- text pravneho predpisu.

Kazdy zaznam hodnot nezavisle od ostatnych.
Nevyzaduj doslovnu zhodu ani rovnaku formulaciu.
Kratka parafraza alebo zhrnutie je v poriadku, ak nemenia pravny vyznam.

Pouzi iba tieto skore:
- 1.0 = text modelu je vecne podporeny pravnym predpisom a nepridava nic podstatne navyse,
- 0.5 = text modelu je iba ciastocne podporeny; jadro je spravne, ale je nepresny, prilis vseobecny alebo miestami doplna nieco, co nie je plne iste,
- 0.0 = text modelu je nepodporeny, skresluje pravny vyznam alebo pripisuje predpisu nieco, co z neho nevyplyva.

V odovodneni pis prirodzene po slovensky. Nevypisuj technicke placeholdery ani nazvy vstupnych blokov.
Pre kazdy zaznam vysvetli:
- co z textu modelu je podlozene,
- co je nepresne alebo nepodlozene,
- preco si zvolil dane skore.

Vrat IBA validny JSON v tomto tvare:
{"results": [{"zakon": "<id>", "score": <0 | 0.5 | 1>, "explanation": "<slovenske odovodnenie>"}]}

Musis vratit presne jeden vysledok pre kazdy vstupny zaznam.
Ziadne dalsie kluce.
""".strip()

SPAN_ALIGNMENT_BATCH_SYSTEM_PROMPT = """
Posudzujes metriku 3 pre viacero pravnych predpisov naraz.

Pre kazdy zaznam dostanes:
- identifikator pravneho predpisu,
- text modelu pre tento predpis,
- relevantnu cast expertnej expected odpovede pre ten isty pravny predpis.

Kazdy zaznam hodnot nezavisle od ostatnych.
Nevyzaduj uplnu vycerpavajucnost.
Kratsi text modelu je v poriadku, ak zachytava spravne jadro pravneho bodu.

Pouzi iba tieto skore:
- 1.0 = text modelu je vecne v sulade s expertne oznacenou castou expected odpovede,
- 0.5 = text modelu je iba ciastocne v sulade; jadro sedi, ale formulacia je nepresna, neuplna alebo mierne posunuta,
- 0.0 = text modelu je v rozpore s expertne oznacenou castou expected odpovede alebo hovori o inom pravnom bode.

V odovodneni pis prirodzene po slovensky. Nevypisuj technicke placeholdery ani nazvy vstupnych blokov.
Pre kazdy zaznam vysvetli:
- v com je zhoda,
- v com je rozdiel,
- preco si zvolil dane skore.

Vrat IBA validny JSON v tomto tvare:
{"results": [{"zakon": "<id>", "score": <0 | 0.5 | 1>, "explanation": "<slovenske odovodnenie>"}]}

Musis vratit presne jeden vysledok pre kazdy vstupny zaznam.
Ziadne dalsie kluce.
""".strip()


def is_refusal_answer(answer: str) -> bool:
    text = safe_str(answer).strip().lower()
    if not text:
        return True
    return any(marker in text for marker in _REFUSAL_MARKERS)


def _trace_set_attr(key: str, value: Any) -> None:
    try:
        from opentelemetry import trace  # type: ignore

        span = trace.get_current_span()
        if span is None:
            return
        if not getattr(span, "is_recording", lambda: False)():
            return
        if isinstance(value, float) and not value.is_integer():
            span.set_attribute(f"{key}_num", float(value))
            span.set_attribute(key, f"{value:.2f}")
            return
        span.set_attribute(key, int(value) if isinstance(value, float) else value)
    except Exception:
        return


def _clip(value: Any, limit: int) -> str:
    text = safe_str(value)
    return text if len(text) <= limit else text[:limit]


@lru_cache(maxsize=1)
def get_judge_client() -> OpenAI:
    return OpenAI(api_key=JUDGE_API_KEY, base_url=JUDGE_BASE_URL)


def _extract_json_object(text: str) -> Optional[Dict[str, Any]]:
    raw = safe_str(text).strip()
    if not raw:
        return None
    if raw.startswith("```"):
        lines = raw.splitlines()
        if lines and lines[0].strip().startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        raw = "\n".join(lines).strip()
        if raw.lower().startswith("json"):
            raw = raw[4:].lstrip()
    start = raw.find("{")
    end = raw.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    try:
        payload = json.loads(raw[start : end + 1])
    except Exception:
        return None
    return payload if isinstance(payload, dict) else None


def _normalize_three_level_score(score: Any) -> float:
    try:
        value = float(score)
    except Exception:
        return 0.0
    value = max(0.0, min(1.0, value))
    if value <= 0.25:
        return 0.0
    if value >= 0.75:
        return 1.0
    return 0.5


def _llm_json_object(system_prompt: str, user_prompt: str) -> Dict[str, Any]:
    client = get_judge_client()
    last_err: Optional[Exception] = None
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model=JUDGE_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.0,
                max_tokens=5000,
            )
            content = safe_str(response.choices[0].message.content).strip()
            payload = _extract_json_object(content)
            if isinstance(payload, dict):
                return payload
            raise ValueError(f"Judge model returned invalid JSON object. Raw output: {_clip(content, 200)}")
        except RateLimitError as exc:
            last_err = exc
            time.sleep(2.0 * (attempt + 1))
        except Exception as exc:
            last_err = exc
            time.sleep(1.0 * (attempt + 1))
    raise RuntimeError(f"Judge LLM failed after 3 retries: {last_err}") from last_err


def _llm_score(system_prompt: str, user_prompt: str) -> Dict[str, Any]:
    client = get_judge_client()
    last_err: Optional[Exception] = None
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model=JUDGE_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.0,
                max_tokens=4096,
            )
            content = safe_str(response.choices[0].message.content).strip()
            payload = _extract_json_object(content)
            if isinstance(payload, dict):
                explanation = safe_str(payload.get("explanation") or payload.get("judge_explanation") or content)
                return {
                    "score": _normalize_three_level_score(payload.get("score", 0.0)),
                    "judge_explanation": _clip(explanation, _JUDGE_EXPLANATION_MAX_CHARS),
                }
            match = _SCORE_RE.search(content)
            if match:
                return {
                    "score": _normalize_three_level_score(match.group(1)),
                    "judge_explanation": _clip(content, _JUDGE_EXPLANATION_MAX_CHARS),
                }
            raise ValueError(f"Judge model returned invalid format. Raw output: {_clip(content, 200)}")
        except RateLimitError as exc:
            last_err = exc
            time.sleep(2.0 * (attempt + 1))
        except Exception as exc:
            last_err = exc
            time.sleep(1.0 * (attempt + 1))
    raise RuntimeError(f"Judge LLM failed after 3 retries: {last_err}") from last_err



def _coerce_batch_results(payload: Dict[str, Any], expected_zakony: List[str]) -> List[Dict[str, Any]]:
    raw_results = payload.get("results")
    if not isinstance(raw_results, list):
        raise ValueError("Judge model did not return a 'results' list.")

    by_zakon: Dict[str, Dict[str, Any]] = {}
    for item in raw_results:
        if not isinstance(item, dict):
            continue
        zakon = safe_str(item.get("zakon")).strip()
        if not zakon or zakon in by_zakon:
            continue
        explanation = safe_str(item.get("explanation") or item.get("judge_explanation")).strip()
        by_zakon[zakon] = {
            "zakon": zakon,
            "score": _normalize_three_level_score(item.get("score", 0.0)),
            "judge_explanation": _clip(explanation, _JUDGE_EXPLANATION_MAX_CHARS),
        }

    out: List[Dict[str, Any]] = []
    for zakon in expected_zakony:
        scored = by_zakon.get(zakon)
        if scored is not None:
            out.append(scored)
            continue
        out.append({
            "zakon": zakon,
            "score": 0.0,
            "judge_explanation": "Sudca nevratil hodnotenie pre tento pravny predpis.",
        })
    return out
def _join_ctx(contexts: List[str]) -> str:
    return _clip("\n\n---\n\n".join(safe_str(value) for value in (contexts or [])), TRIAD_MAX_CHARS)


def groundedness_score(question: str, answer: str, contexts: List[str]) -> Dict[str, Any]:
    q = safe_str(question)
    a = safe_str(answer)
    ctx = _join_ctx(contexts)
    if not q or not a or not ctx:
        return {"score": 0.0, "judge_explanation": "Chyba otazka, odpoved alebo context."}
    return _llm_score(
        GROUNDEDNESS_SYSTEM_PROMPT,
        f"QUESTION:\n{q}\n\nCONTEXT:\n{ctx}\n\nANSWER:\n{a}\n",
    )



def extract_marked_statute_context_local(text: str) -> Dict[str, Any]:
    source = safe_str(text).strip()
    if not source:
        return {"span": "", "judge_explanation": "Chyba vstupny text."}
    if "***" not in source:
        return {"span": "", "judge_explanation": "V expected odpovedi nebolo oznacenie cieloveho pravneho predpisu."}

    matches = list(re.finditer(r"\*\*\*.*?\*\*\*", source, flags=re.DOTALL))
    if not matches:
        return {"span": "", "judge_explanation": "V expected odpovedi sa nenasla oznacena citacia tohto pravneho predpisu."}

    excerpts: List[str] = []
    for match in matches:
        start = max(0, match.start() - 450)
        end = min(len(source), match.end() + 450)

        while start > 0 and source[start - 1] not in ".!?\n":
            start -= 1
        while end < len(source) and source[end - 1] not in ".!?\n":
            end += 1

        excerpt = source[start:end].replace("***", "").strip()
        if excerpt and excerpt not in excerpts:
            excerpts.append(excerpt)

    span = _clip("\n\n...\n\n".join(excerpts), TRIAD_MAX_CHARS)
    if not span:
        return {"span": "", "judge_explanation": "Nepodarilo sa lokalne vyrezat pouzitelny expert span."}
    return {"span": span, "judge_explanation": "Relevantna cast expected odpovede bola vyrezana lokalne z oznaceneho textu."}


def answer_span_faithfulness_batch_score(question: str, items: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    del question
    normalized_items: List[Dict[str, str]] = []
    for item in items:
        zakon = safe_str(item.get("zakon")).strip()
        model_text = safe_str(item.get("model_span")).strip()
        legal_text = safe_str(item.get("provision_text")).strip()
        if not zakon or not model_text or not legal_text:
            continue
        normalized_items.append({
            "zakon": zakon,
            "text_modelu": _clip(model_text, TRIAD_MAX_CHARS),
            "text_pravneho_predpisu": _clip(legal_text, TRIAD_MAX_CHARS),
        })

    if not normalized_items:
        return []

    payload = _llm_json_object(
        SPAN_FAITHFULNESS_BATCH_SYSTEM_PROMPT,
        "ZAZNAMY_NA_HODNOTENIE:\n" + json.dumps(normalized_items, ensure_ascii=False, indent=2),
    )
    return _coerce_batch_results(payload, [item["zakon"] for item in normalized_items])


def citation_expected_alignment_batch_score(question: str, items: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    q = safe_str(question).strip()
    normalized_items: List[Dict[str, str]] = []
    for item in items:
        zakon = safe_str(item.get("zakon")).strip()
        model_text = safe_str(item.get("model_span")).strip()
        expected_text = safe_str(item.get("expected_span")).strip()
        if not zakon or not model_text or not expected_text:
            continue
        normalized_items.append({
            "zakon": zakon,
            "text_modelu": _clip(model_text, TRIAD_MAX_CHARS),
            "relevantna_cast_expertnej_expected_odpovede": _clip(expected_text, TRIAD_MAX_CHARS),
        })

    if not normalized_items:
        return []

    payload = _llm_json_object(
        SPAN_ALIGNMENT_BATCH_SYSTEM_PROMPT,
        f"QUESTION:\n{q}\n\nZAZNAMY_NA_HODNOTENIE:\n" + json.dumps(normalized_items, ensure_ascii=False, indent=2),
    )
    return _coerce_batch_results(payload, [item["zakon"] for item in normalized_items])
def _split_zakon_id(zakon: Any) -> tuple[str, str]:
    raw = safe_str(zakon).strip()
    match = _ZAKON_ID_PARTS_RE.fullmatch(raw)
    if not match:
        return "", ""
    return match.group("law"), match.group("paragraph").lower()


def _mark_pattern(text: str, pattern: str) -> tuple[str, int]:
    count = 0

    def _repl(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        value = match.group(0)
        if value.startswith("***") and value.endswith("***"):
            return value
        return f"***{value}***"

    return re.sub(pattern, _repl, text, flags=re.IGNORECASE), count


def mark_target_zakon_refs(text: str, zakon: str, provisions: Optional[List[Dict[str, Any]]] = None) -> str:
    source = safe_str(text)
    if not source:
        return ""

    law_id, paragraph = _split_zakon_id(zakon)
    if not law_id or not paragraph:
        return source

    sections: List[str] = []
    for item in provisions or []:
        if not isinstance(item, dict):
            continue
        if build_zakon_id(item.get("law"), item.get("paragraph")) != safe_str(zakon).strip():
            continue
        section = safe_str(item.get("section")).strip()
        if section and section not in sections:
            sections.append(section)

    short_name = _LAW_SHORT_NAMES.get(law_id, "")
    prefix = rf"(?:§|paragraf(?:u|om)?)\s*{re.escape(paragraph)}"
    section_patterns = [
        rf"{prefix}\s*ods\.\s*{re.escape(section)}(?:\s*a\s*nasl\.)?"
        for section in sections
    ]
    generic_pattern = rf"{prefix}(?:\s*ods\.\s*\d+)?(?:\s*a\s*nasl\.)?"

    if short_name:
        with_law = section_patterns + [generic_pattern]
        combined_with_law = "|".join(rf"(?:{pattern})\s*{re.escape(short_name)}" for pattern in with_law)
        marked, count = _mark_pattern(source, combined_with_law)
        if count > 0:
            return marked

    combined_generic = "|".join(section_patterns + [generic_pattern])
    marked, count = _mark_pattern(source, combined_generic)
    return marked if count > 0 else source


def extract_marked_statute_context(text: str, zakon: str) -> Dict[str, Any]:
    source = safe_str(text).strip()
    zakon_id = safe_str(zakon).strip()
    if not source or not zakon_id:
        return {"span": "", "judge_explanation": "Chyba vstupny text alebo identifikator pravneho predpisu."}
    if "***" not in source:
        return {"span": "", "judge_explanation": "V expected odpovedi nebolo oznacenie cieloveho pravneho predpisu."}

    payload = _llm_json_object(
        STATUTE_CONTEXT_EXTRACTION_SYSTEM_PROMPT,
        f"ZAKON_ID:\n{zakon_id}\n\nFULL_TEXT:\n{_clip(source, TRIAD_MAX_CHARS)}\n",
    )
    span = _clip(safe_str(payload.get("span")).strip(), TRIAD_MAX_CHARS)
    reason = _clip(
        safe_str(payload.get("reason") or payload.get("judge_explanation") or payload.get("explanation")).strip(),
        _JUDGE_EXPLANATION_MAX_CHARS,
    )
    return {"span": span, "judge_explanation": reason}


def citation_expected_alignment_score(question: str, zakon: str, model_span: str, expected_span: str) -> Dict[str, Any]:
    q = safe_str(question).strip()
    zakon_id = safe_str(zakon).strip()
    model_text = safe_str(model_span).strip()
    expected_text = safe_str(expected_span).strip()
    if not zakon_id or not model_text or not expected_text:
        return {"score": 0.0, "judge_explanation": "Chyba text modelu, gold span alebo identifikator pravneho predpisu."}

    user_prompt = (
        f"QUESTION:\n{q}\n\n"
        f"ZAKON_ID:\n{zakon_id}\n\n"
        f"RELEVANTNA_CAST_EXPERTNEJ_EXPECTED_ODPOVEDE:\n{_clip(expected_text, TRIAD_MAX_CHARS)}\n\n"
        f"TEXT_MODELU_PRE_TENTO_PREDPIS:\n{_clip(model_text, TRIAD_MAX_CHARS)}\n"
    )
    return _llm_score(SPAN_ALIGNMENT_SYSTEM_PROMPT, user_prompt)


def answer_span_faithfulness_score(question: str, zakon: str, model_span: str, provision_text: str) -> Dict[str, Any]:
    del question
    zakon_id = safe_str(zakon).strip()
    model_text = safe_str(model_span).strip()
    legal_text = safe_str(provision_text).strip()
    if not zakon_id or not model_text or not legal_text:
        return {"score": 0.0, "judge_explanation": "Chyba text modelu, text pravneho predpisu alebo identifikator pravneho predpisu."}

    user_prompt = (
        f"ZAKON_ID:\n{zakon_id}\n\n"
        f"TEXT_PRAVNEHO_PREDPISU:\n{_clip(legal_text, TRIAD_MAX_CHARS)}\n\n"
        f"TEXT_MODELU_PRE_TENTO_PREDPIS:\n{_clip(model_text, TRIAD_MAX_CHARS)}\n"
    )
    return _llm_score(SPAN_FAITHFULNESS_SYSTEM_PROMPT, user_prompt)


@scorer(name="triad_groundedness")
def triad_groundedness_scorer(inputs: dict | str | None = None, outputs: dict | None = None, **_: dict) -> float:
    if outputs is None:
        _trace_set_attr("m.triad_groundedness", 0.0)
        return 0.0

    q_id = -1
    question = ""
    if isinstance(inputs, dict):
        q_id = int(inputs.get("id")) if str(inputs.get("id", "")).isdigit() else -1
        question = safe_str(inputs.get("question"))
    else:
        question = safe_str(inputs)

    answer = safe_str(outputs.get("answer") or outputs.get("response") or outputs.get("prediction"))
    if is_refusal_answer(answer):
        TRIAD_JUDGE_LOG.append(
            {"id": q_id, "question": question, "answer": answer, "triad_groundedness": 0.0, "judge_explanation": "REFUSAL"}
        )
        _trace_set_attr("m.triad_groundedness", 0.0)
        return 0.0

    context_docs = outputs.get("context_docs") or []
    if not isinstance(context_docs, list):
        context_docs = [context_docs]

    pkg = groundedness_score(question, answer, [safe_str(value) for value in context_docs])
    score = float(max(0.0, min(1.0, float(pkg.get("score", 0.0)))))
    TRIAD_JUDGE_LOG.append(
        {
            "id": q_id,
            "question": question,
            "answer": answer,
            "triad_groundedness": score,
            "judge_explanation": _clip(safe_str(pkg.get("judge_explanation")), _JUDGE_EXPLANATION_MAX_CHARS),
        }
    )
    _trace_set_attr("m.triad_groundedness", score)
    return score


def re_split_sentences(text: str) -> List[str]:
    value = safe_str(text).strip()
    if not value:
        return []
    out: List[str] = []
    current: List[str] = []
    for char in value:
        current.append(char)
        if char in ".!?":
            out.append("".join(current).strip())
            current = []
    if current:
        out.append("".join(current).strip())
    return out