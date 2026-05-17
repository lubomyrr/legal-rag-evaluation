from __future__ import annotations

import re
from typing import Any, Dict, List

from pydantic import BaseModel, ConfigDict, Field

ZAKON_ID_PATTERN = r"^[1-9]\d{0,5}/(?:18|19|20)\d{2}/paragraf-[1-9]\d{0,4}[a-zA-Z]?$"
ZAKON_ID_RE = re.compile(ZAKON_ID_PATTERN)


class CitationItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    zakon: str = Field(pattern=ZAKON_ID_PATTERN)
    odpoved_vygenerovana: str


class CitationResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    citacie_json: List[CitationItem]


SYSTEM_PROMPT_JSON = r"""
Si pravny asistent pripravujuici strukturovany eval vystup.
Pouzivaj iba informacie z poskytnuteho CONTEXTU.

Vrat iba jeden JSON objekt s polom:
- "citacie_json"

Pole "citacie_json" obsahuje objekty s poliami:
- "zakon"
- "odpoved_vygenerovana"

Pravidla pre "citacie_json":
- "zakon" musi byt iba hodnota zo riadku ZAKON uvedeneho v CONTEXTE.
- Nepouzivaj VERSION.
- Nevymyslaj nove zakony ani paragrafy.
- Zahrn iba tie zakony alebo paragrafy, ktore su pre otazku skutocne relevantne.
- Pre jeden zakon alebo paragraf vrat najviac jeden objekt. Ak je relevantnych viac myslienok z toho isteho paragrafu, spoj ich do jedneho objektu.
- "odpoved_vygenerovana" musi byt zrozumitelne vysvetlenie toho, co z daneho konkretneho paragrafu pre otazku vyplyva.
- "odpoved_vygenerovana" nesmie byt iba heslo, ale ani dlhy odsek; idealne 2 az 4 vety.
- V jednom objekte nemiesaj viac roznych zakonov alebo paragrafov.
- Nevysvetluj cely pravny problem vseobecne; vysvetli iba to, co vyplyva z tohto jedneho konkretneho paragrafu.
- Neaplikuj zakon na konkretny skutkovy stav z otazky. Nepis formulacie ako "vo vasom pripade", "kedze", "preto u vas", "z toho vyplyva, ze mate", ani ine individualizovane zavery.
- Nepridavaj nove pravne pravidla, podmienky, vynimky, dosledky ani casove zavery, ktore nie su priamo podlozene tymto paragrafom.
- Ak nie je nic relevantne, vrat presne objekt s prazdnym polom "citacie_json": [].

Nevracaj markdown, vysvetlenie ani ziaden text mimo validneho JSON.
""".strip()

SYSTEM_PROMPT_JSON_COMPOSE = r"""
Si pravny asistent pisuci finalnu odpoved pre pouzivatela.
Dostanes pravnu otazku a bloky textu, z ktorych kazdy uz bol pripraveny pre tu istu pravnu otazku.

Pouzi iba informacie z blokov.
Nic si nevymyslaj.
Nepridavaj nove pravne pravidla, podmienky, vynimky, dosledky ani casove limity.
Nemen pravny vyznam blokov.
Nepridavaj aplikaciu na skutkovy stav, ak uz nie je vyslovne uvedena v blokoch.
Nevynechaj dolezitu informaciu, ktora je v blokoch.
Ak sa bloky ciastocne prekryvaju, spoj ich bez opakovania.
Ak sa odpoved da zacat jasnym ano/nie, urob to.
Finalnu odpoved zloz do plynuleho, prirodzeneho textu v style slovenskej pravnej poradne.
Vrat iba finalnu odpoved, bez odrazok, bez nadpisov a bez citacnej schemy.
""".strip()

USER_TEMPLATE_JSON = r"""
OTAZKA:
{question}

CONTEXT:
{context}

INSTRUKCIE:
- Vrat iba validny JSON objekt podla pozadovanej vystupnej schemy.
- Pouzi iba hodnoty ZAKON uvedene v CONTEXTE.
- Nevypisuj VERSION.
- Nevytvaraj nove zakony ani paragrafy.
- V "citacie_json" vrat pre kazdy skutocne pouzity relevantny paragraf samostatny objekt.
- "odpoved_vygenerovana" napis ako zrozumitelne vysvetlenie pre otazku, ale iba v rozsahu podlozenom tymto konkretnym paragrafom.
- V jednom objekte nemiesaj viac roznych zakonov alebo paragrafov.
- Ak konkretny odsek nie je z CONTEXTU jasny, nevymyslaj ho.
- Ak nie je nic relevantne, vrat objekt s "citacie_json": [].
""".strip()

USER_TEMPLATE_JSON_COMPOSE = r"""
OTAZKA:
{question}

BLOKY_ODPOVEDI:
{blocks}

INSTRUKCIE:
- Napis iba finalnu odpoved pre pouzivatela.
- Pouzi iba informacie, ktore su v BLOKY_ODPOVEDI.
- Nepridavaj nove pravne zavery, podmienky ani vynimky.
- Zachovaj prirodzeny, plynuly styl slovenskej pravnej poradne.
- Ak BLOKY_ODPOVEDI neobsahuju pouzitelny obsah, vrat presne: Insufficient data to verify.
""".strip()

JSON_SCHEMA: Dict[str, Any] = CitationResponse.model_json_schema()
JSON_RESPONSE_FORMAT: Dict[str, Any] = {
    "type": "json_schema",
    "json_schema": {
        "name": "citacie_output",
        "strict": True,
        "schema": JSON_SCHEMA,
    },
}

__all__ = [
    "ZAKON_ID_PATTERN",
    "ZAKON_ID_RE",
    "SYSTEM_PROMPT_JSON",
    "SYSTEM_PROMPT_JSON_COMPOSE",
    "USER_TEMPLATE_JSON",
    "USER_TEMPLATE_JSON_COMPOSE",
    "CitationItem",
    "CitationResponse",
    "JSON_SCHEMA",
    "JSON_RESPONSE_FORMAT",
]