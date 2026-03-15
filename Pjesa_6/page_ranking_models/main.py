from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List, Optional

from ranking.ranking_engine import rank_pages
from visualization.plot_scores import plot_final_scores
from visualization.graph_plot import plot_web_graph


def load_pages(path: str) -> List[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_personalization(pages: List[dict], topic: Optional[str]) -> Optional[Dict[str, float]]:
    if topic is None:
        return None

    topic = topic.lower().strip()
    personalization = {}

    for page in pages:
        text = " ".join([
            page.get("title", ""),
            page.get("content", ""),
            " ".join(page.get("tags", [])),
        ]).lower()
        personalization[page["id"]] = 2.0 if topic in text else 0.5

    return personalization


def print_results(results: List[dict]) -> None:
    print("\nRenditja finale e faqeve\n" + "-" * 72)
    for i, item in enumerate(results, start=1):
        print(
            f"{i:>2}. {item['title']}\n"
            f"    id={item['id']}, score={item['final_score']:.4f}, "
            f"PR={item['pagerank']:.4f}, rel={item['relevance_norm']:.3f}, "
            f"fresh={item['freshness_norm']:.3f}, qual={item['quality_norm']:.3f}, "
            f"user={item['user_norm']:.3f}, spam={item['spam_norm']:.3f}\n"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Algoritëm hibrid për renditjen e faqeve në web."
    )
    parser.add_argument(
        "--data",
        type=str,
        default="examples/sample_pages.json",
        help="Skedari JSON me faqet dhe lidhjet.",
    )
    parser.add_argument(
        "--query",
        type=str,
        default="fizike algoritme",
        help="Pyetja e përdoruesit.",
    )
    parser.add_argument(
        "--alpha",
        type=float,
        default=0.85,
        help="Faktori i amortizimit për PageRank.",
    )
    parser.add_argument(
        "--topic",
        type=str,
        default=None,
        help="Temë për personalized PageRank, p.sh. 'fizike' ose 'ai'.",
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help="Ruaj grafikët e score-ve dhe të grafit të faqeve.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pages = load_pages(args.data)
    personalization = build_personalization(pages, args.topic)

    results = rank_pages(
        pages=pages,
        query=args.query,
        alpha=args.alpha,
        personalization=personalization,
    )
    print_results(results)

    if args.plot:
        out1 = plot_final_scores(results, output="ranking_scores.png")
        out2 = plot_web_graph(pages, output="web_graph.png")
        print(f"U ruajt grafiku i score-ve: {out1}")
        print(f"U ruajt grafiku i web-it: {out2}")


if __name__ == "__main__":
    main()
