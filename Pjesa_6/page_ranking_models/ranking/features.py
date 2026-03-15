from __future__ import annotations

from typing import Dict, Iterable, List
from datetime import datetime
import math
import re


WORD_RE = re.compile(r"\w+", flags=re.UNICODE)


def tokenize(text: str) -> List[str]:
    return [t.lower() for t in WORD_RE.findall(text)]


def compute_text_relevance(query: str, page: dict) -> float:
    """
    Model i thjeshtë relevance:
    - përputhje në titull
    - përputhje në trup
    - bonus për etiketat/temat
    """
    query_tokens = tokenize(query)
    if not query_tokens:
        return 0.0

    title_tokens = tokenize(page.get("title", ""))
    body_tokens = tokenize(page.get("content", ""))
    tag_tokens = tokenize(" ".join(page.get("tags", [])))

    score = 0.0
    for token in query_tokens:
        score += 3.0 * title_tokens.count(token)
        score += 1.0 * body_tokens.count(token)
        score += 2.0 * tag_tokens.count(token)

    # Bonus i thjeshtë për mbulim të plotë të pyetjes.
    coverage = sum(1 for token in set(query_tokens) if token in title_tokens or token in body_tokens or token in tag_tokens)
    score += 1.5 * coverage

    return score


def compute_freshness(last_updated: str, current_date: str = "2026-03-15", decay: float = 0.015) -> float:
    """
    Freski eksponenciale:
    F = exp(-decay * delta_days)
    """
    try:
        d_now = datetime.fromisoformat(current_date)
        d_page = datetime.fromisoformat(last_updated)
    except ValueError:
        return 0.0

    delta_days = max((d_now - d_page).days, 0)
    return math.exp(-decay * delta_days)


def normalize_dict(values: Dict[str, float]) -> Dict[str, float]:
    """
    Normalizim min-max në [0, 1].
    """
    if not values:
        return {}

    vals = list(values.values())
    vmin = min(vals)
    vmax = max(vals)

    if math.isclose(vmin, vmax):
        return {k: 1.0 for k in values}

    return {k: (v - vmin) / (vmax - vmin) for k, v in values.items()}
