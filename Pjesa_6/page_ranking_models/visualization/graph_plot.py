from __future__ import annotations

from pathlib import Path
from typing import List
import matplotlib.pyplot as plt
import networkx as nx


def plot_web_graph(pages: List[dict], output: str = "web_graph.png") -> Path:
    G = nx.DiGraph()

    for page in pages:
        G.add_node(page["id"], label=page.get("title", page["id"]))
        for dst in page.get("links_to", []):
            G.add_edge(page["id"], dst)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx(G, pos, with_labels=True, node_size=1800, font_size=9, arrows=True)
    plt.title("Grafi i faqeve dhe lidhjeve")
    plt.axis("off")
    plt.tight_layout()

    output_path = Path(output)
    plt.savefig(output_path, dpi=150)
    plt.close()
    return output_path
