import matplotlib.pyplot as plt
import networkx as nx
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


def drawGraph(
    G: nx.DiGraph,
    position: dict[str, Point],
    edgeLabels: dict[tuple[str, str], str],
    A: list[tuple[str, str]]|None,
):
    font_size = 24
    node_size = 5000
    edge_width = 5.0
    node_color = "c"
    arrowsize = 50
    plt.figure(figsize=(15, 20), facecolor="white")
    plt.subplot(2, 1, 1)
    nx.draw_networkx_nodes(G, position, node_size=node_size, node_color=node_color)
    nx.draw_networkx_labels(G, position, font_size=font_size)
    nx.draw_networkx_edges(
        G,
        position,
        width=edge_width,
        arrows=True,
        arrowsize=arrowsize,
        node_size=node_size,
    )
    nx.draw_networkx_edge_labels(
        G, position, edge_labels=edgeLabels, font_size=font_size
    )
    plt.axis("off")
    if A:
        plt.subplot(2, 1, 2)
        nx.draw_networkx_nodes(G, position, node_size=node_size, node_color=node_color)
        nx.draw_networkx_labels(G, position, font_size=font_size)
        nx.draw_networkx_edges(
            G,
            position,
            A,
            width=edge_width,
            edge_color="r",
            arrows=True,
            arrowsize=arrowsize,
            node_size=node_size,
        )

        plt.axis("off")
    plt.show()
