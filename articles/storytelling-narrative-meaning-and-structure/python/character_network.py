"""
Storytelling: Character Relationship Network

Educational workflow for modeling character roles, relationships,
and simple network diagnostics.
"""

from __future__ import annotations

import pandas as pd
import networkx as nx


def build_character_graph(characters: pd.DataFrame, relationships: pd.DataFrame) -> nx.DiGraph:
    """Build a directed graph of character relationships."""
    graph = nx.DiGraph()

    for _, row in characters.iterrows():
        graph.add_node(row["character"], role=row["role"])

    for _, row in relationships.iterrows():
        graph.add_edge(row["source"], row["target"], relationship=row["relationship"])

    return graph


def graph_metrics(graph: nx.DiGraph) -> pd.DataFrame:
    """Calculate simple network metrics for character relationships."""
    centrality = nx.degree_centrality(graph)

    return pd.DataFrame({
        "character": list(graph.nodes()),
        "role": [graph.nodes[node]["role"] for node in graph.nodes()],
        "in_degree": [graph.in_degree(node) for node in graph.nodes()],
        "out_degree": [graph.out_degree(node) for node in graph.nodes()],
        "degree_centrality": [centrality[node] for node in graph.nodes()]
    }).sort_values("degree_centrality", ascending=False)


def main() -> None:
    characters = pd.read_csv("../data/characters.csv")
    relationships = pd.read_csv("../data/relationships.csv")

    characters["transformation_score"] = (
        characters["final_state"] - characters["initial_state"]
    )

    graph = build_character_graph(characters, relationships)
    metrics = graph_metrics(graph)

    print(characters)
    print(metrics)

    characters.to_csv("../outputs/character_arcs.csv", index=False)
    metrics.to_csv("../outputs/character_network_metrics.csv", index=False)


if __name__ == "__main__":
    main()
