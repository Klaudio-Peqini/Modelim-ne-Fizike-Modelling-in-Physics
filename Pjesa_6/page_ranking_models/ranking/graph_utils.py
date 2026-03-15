from __future__ import annotations

from typing import Dict, List, Tuple
import numpy as np


def pages_to_index_map(pages: List[dict]) -> Dict[str, int]:
    """
    Kthen hartën page_id -> indeks matricor.
    """
    return {page["id"]: i for i, page in enumerate(pages)}


def build_adjacency_matrix(pages: List[dict]) -> Tuple[np.ndarray, List[str]]:
    """
    Ndërton matricën e tranzicionit kolonë-stokastike për PageRank.

    Konventa:
    - Nëse faqja j lidhet me faqen i, atëherë M[i, j] > 0.
    - Kolona j përmban probabilitetet e lëvizjes nga faqja j
      drejt faqeve të tjera.
    - Nyjet pa lidhje dalëse trajtohen si dangling nodes dhe
      zëvendësohen me shpërndarje uniforme.
    """
    n = len(pages)
    ids = [page["id"] for page in pages]
    index = pages_to_index_map(pages)

    M = np.zeros((n, n), dtype=float)

    for src_page in pages:
        j = index[src_page["id"]]
        out_links = [dst for dst in src_page.get("links_to", []) if dst in index]

        if len(out_links) == 0:
            M[:, j] = 1.0 / n
            continue

        weight = 1.0 / len(out_links)
        for dst_id in out_links:
            i = index[dst_id]
            M[i, j] += weight

    return M, ids
