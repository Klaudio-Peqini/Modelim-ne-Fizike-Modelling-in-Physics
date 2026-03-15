from __future__ import annotations

from typing import Dict, List, Optional

from .graph_utils import build_adjacency_matrix
from .pagerank import pagerank, personalized_pagerank
from .features import compute_text_relevance, compute_freshness, normalize_dict


def rank_pages(
    pages: List[dict],
    query: str,
    alpha: float = 0.85,
    personalization: Optional[Dict[str, float]] = None,
    weights: Optional[Dict[str, float]] = None,
) -> List[dict]:
    """
    Rendit faqet sipas një score hibrid:
        score =
            w_pagerank * PageRank
          + w_relevance * Relevance
          + w_freshness * Freshness
          + w_quality   * Quality
          + w_user      * UserSignals
          - w_spam      * Spam

    Të gjithë komponentët normalizohen paraprakisht në [0,1].
    """
    if weights is None:
        weights = {
            "pagerank": 0.30,
            "relevance": 0.30,
            "freshness": 0.10,
            "quality": 0.15,
            "user": 0.10,
            "spam": 0.05,
        }

    M, ids = build_adjacency_matrix(pages)

    if personalization is None:
        pr = pagerank(M, ids, alpha=alpha)
    else:
        pr = personalized_pagerank(M, ids, personalization=personalization, alpha=alpha)

    relevance = {page["id"]: compute_text_relevance(query, page) for page in pages}
    freshness = {page["id"]: compute_freshness(page.get("last_updated", "2025-01-01")) for page in pages}
    quality = {page["id"]: float(page.get("quality_score", 0.0)) for page in pages}
    user = {page["id"]: float(page.get("user_signal", 0.0)) for page in pages}
    spam = {page["id"]: float(page.get("spam_score", 0.0)) for page in pages}

    pr_n = normalize_dict(pr)
    rel_n = normalize_dict(relevance)
    fresh_n = normalize_dict(freshness)
    quality_n = normalize_dict(quality)
    user_n = normalize_dict(user)
    spam_n = normalize_dict(spam)

    results = []
    for page in pages:
        pid = page["id"]
        final_score = (
            weights["pagerank"] * pr_n[pid]
            + weights["relevance"] * rel_n[pid]
            + weights["freshness"] * fresh_n[pid]
            + weights["quality"] * quality_n[pid]
            + weights["user"] * user_n[pid]
            - weights["spam"] * spam_n[pid]
        )

        results.append(
            {
                "id": pid,
                "title": page.get("title", pid),
                "final_score": final_score,
                "pagerank": pr[pid],
                "pagerank_norm": pr_n[pid],
                "relevance_norm": rel_n[pid],
                "freshness_norm": fresh_n[pid],
                "quality_norm": quality_n[pid],
                "user_norm": user_n[pid],
                "spam_norm": spam_n[pid],
                "links_to": page.get("links_to", []),
                "last_updated": page.get("last_updated", ""),
            }
        )

    results.sort(key=lambda x: x["final_score"], reverse=True)
    return results
