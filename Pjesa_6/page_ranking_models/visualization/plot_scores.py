from __future__ import annotations

from pathlib import Path
from typing import List
import matplotlib.pyplot as plt


def plot_final_scores(results: List[dict], output: str = "ranking_scores.png") -> Path:
    titles = [r["title"] for r in results]
    scores = [r["final_score"] for r in results]

    plt.figure(figsize=(10, 5))
    plt.bar(titles, scores)
    plt.xticks(rotation=35, ha="right")
    plt.ylabel("Score final")
    plt.title("Renditja finale e faqeve")
    plt.tight_layout()

    output_path = Path(output)
    plt.savefig(output_path, dpi=150)
    plt.close()
    return output_path
