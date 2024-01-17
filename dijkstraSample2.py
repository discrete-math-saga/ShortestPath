import networkx as nx
from dijkstra import Dijkstra
from drawGraph import drawGraph, Point


def defineGraph() -> tuple[nx.DiGraph, dict[str, Point], dict[tuple[str, str], str]]:
    numNode = 7
    nodeList = list()
    for i in range(8):
        nodeList.append(f"v{i}")

    edgeListWithWeight: list[tuple[str, str, float]] = [
        ("v0", "v1", 1),
        ("v0", "v3", 1),
        ("v1", "v2", 2),
        ("v1", "v4", 3),
        ("v2", "v5", 3),
        ("v2", "v6", 1),
        ("v3", "v4", 2),
        ("v4", "v0", 1),
        ("v4", "v5", 1),
        ("v4", "v7", 1),
        ("v5", "v1", 1),
        ("v6", "v5", 2),
        ("v6", "v7", 1),
        ("v7", "v3", 2),
        ("v7", "v5", 1),
    ]
    edgeLabels: dict[tuple[str, str], str] = dict()
    position: dict[str, Point] = {
        "v0": Point(0.2, 0.4),
        "v1": Point(0, 0),
        "v2": Point(0.2, -0.4),
        "v3": Point(0.6, 0.4),
        "v4": Point(0.4, 0.2),
        "v5": Point(0.4, -0.2),
        "v6": Point(0.6, -0.4),
        "v7": Point(0.8, 0.0),
    }
    G = nx.DiGraph()
    G.add_nodes_from(nodeList)
    for s, d, w in edgeListWithWeight:
        a = (s, d)
        G.add_edge(s, d, weight=w)
        edgeLabels[a] = str(w)
    return G, position, edgeLabels


if __name__ == "__main__":
    G, position, edgeLabels = defineGraph()
    A: list[tuple[str, str]] = Dijkstra(G, "v0")
    drawGraph(G, position, edgeLabels, A)
