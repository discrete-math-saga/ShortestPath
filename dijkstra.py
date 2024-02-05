import networkx as nx
# import sys
import math
from binaryHeap import BinaryHeap


class P:
    def __init__(self, label: str, value: float):
        self.label = label
        self.value = value

    def __lt__(self, o):
        return self.value < o.value

    def __str__(self):
        return f"{self.label}:{self.value}"


def Dijkstra(G: nx.DiGraph, start: str) -> list[tuple[str, str]]:
    p:dict[str,P] = dict()
    q:dict[str,str|None] = dict()
    for v in G.nodes:
        p[v] = P(v, math.inf)
        q[v] = None
    p[start].value = 0
    U = BinaryHeap[P]()
    for k in p.keys():
        U.add(p[k])

    while U.size() > 0:
        u = U.poll()
        if u:
            w = u.label
            for s, x in nx.edges(G, w):
                if p[x].value > p[w].value + G.edges[s, x]["weight"]:
                    q[x] = w
                    p[x].value = p[w].value + G.edges[s, x]["weight"]
                    U.reduceValue(p[x])
    # 経路の取り出し
    A = list()
    for t in q.keys():
        f = q[t]
        if not (f is None):
            A.append((f, t))
    return A

def FloydMarshall(G: nx.DiGraph) -> dict[tuple[str,str],float]:
    res:dict[tuple[str,str],float] = dict()
    for u in G.nodes:
        for v in G.nodes:
            res[(u,v)] = math.inf
        res[(u,u)]=0.
    for u,v in G.edges:
        res[(u,v)] = G.edges[(u,v)]['weight']

    for t in G.nodes:
        for u in G.nodes:
            for v in G.nodes:
                res[(u,v)] = min(res[u,v],res[u,t]+res[t,v])       
    return res
