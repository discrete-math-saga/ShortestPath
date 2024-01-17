import networkx as nx
from dijkstra import Dijkstra
from drawGraph import drawGraph, Point


def defineGraph() -> tuple[nx.DiGraph, dict[str, Point], dict[tuple[str, str], str]]:
    numNode = 7
    nodeList = list()
    for i in range(7):
        nodeList.append(f"v{i}")

    edgeListWithWeight: list[tuple[str, str, float]] = [
        ("v0", "v1", 2),
        ("v0", "v2", 1),
        ("v1", "v4", 3),
        ("v2", "v3", 2),
        ("v2", "v6", 3),
        ("v3", "v1", 1),
        ("v3", "v4", 1),
        ("v3", "v5", 3),
        ("v4", "v5", 1),
        ("v5", "v6", 1),
        ("v6", "v3", 1),
    ]
    edgeLabels: dict[tuple[str, str], str] = dict()
    position: dict[str, Point] = {
        "v0": Point(0.2, 0.8),
        "v1": Point(0.4, 0.8),
        "v2": Point(0.2, 0.6),
        "v3": Point(0.4, 0.6),
        "v4": Point(0.6, 0.8),
        "v5": Point(0.6, 0.6),
        "v6": Point(0.4, 0.4),
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
    A = Dijkstra(G, "v0")
    drawGraph(G, position, edgeLabels, A)
