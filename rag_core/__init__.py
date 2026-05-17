from __future__ import annotations

__version__ = "0.1.0"

def run_eval(*args, **kwargs):
    from . import eval_local as _m
    fn = getattr(_m, "run_eval", None) or getattr(_m, "main", None)
    if fn is None:
        raise AttributeError("eval_local.py must define run_eval() or main().")
    return fn(*args, **kwargs)

def main():
    from . import eval_local as _m
    fn = getattr(_m, "main", None) or getattr(_m, "run_eval", None)
    if fn is None:
        raise AttributeError("eval_local.py must define main() or run_eval().")
    return fn()

__all__ = ["__version__", "run_eval", "main"]