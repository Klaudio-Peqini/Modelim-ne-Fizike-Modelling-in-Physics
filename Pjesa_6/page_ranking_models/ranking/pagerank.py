from __future__ import annotations

from typing import Dict, List, Optional
import numpy as np


def _prepare_personalization(ids: List[str], personalization: Optional[Dict[str, float]]) -> np.ndarray:
    n = len(ids)

    if personalization is None:
        return np.full(n, 1.0 / n, dtype=float)

    v = np.array([max(0.0, float(personalization.get(pid, 0.0))) for pid in ids], dtype=float)

    if np.allclose(v.sum(), 0.0):
        return np.full(n, 1.0 / n, dtype=float)

    return v / v.sum()


def pagerank(
    M: np.ndarray,
    ids: List[str],
    alpha: float = 0.85,
    tol: float = 1e-10,
    max_iter: int = 500,
) -> Dict[str, float]:
    """
    PageRank klasik me teleportim uniform.
    """
    return personalized_pagerank(
        M=M,
        ids=ids,
        personalization=None,
        alpha=alpha,
        tol=tol,
        max_iter=max_iter,
    )


def personalized_pagerank(
    M: np.ndarray,
    ids: List[str],
    personalization: Optional[Dict[str, float]] = None,
    alpha: float = 0.85,
    tol: float = 1e-10,
    max_iter: int = 500,
) -> Dict[str, float]:
    """
    Personalized PageRank me metodën e iterimit të fuqisë.
    """
    n = len(ids)
    if M.shape != (n, n):
        raise ValueError("Matrica M duhet të jetë me përmasa n x n.")

    v = _prepare_personalization(ids, personalization)
    r = np.full(n, 1.0 / n, dtype=float)

    for _ in range(max_iter):
        r_next = alpha * (M @ r) + (1.0 - alpha) * v
        if np.linalg.norm(r_next - r, ord=1) < tol:
            r = r_next
            break
        r = r_next

    r = r / r.sum()
    return {pid: float(score) for pid, score in zip(ids, r)}
