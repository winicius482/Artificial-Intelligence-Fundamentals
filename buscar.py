import networkx as nx
import math

def heuristica(a, b, pos):
    (x1, y1) = pos[a]
    (x2, y2) = pos[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def criar_grafo():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ("Centro", "A", 5),
        ("Centro", "B", 8),
        ("A", "C", 4),
        ("B", "C", 3),
        ("C", "D", 6),
    ])

    pos = {
        "Centro": (0,0),
        "A": (1,2),
        "B": (2,1),
        "C": (3,3),
        "D": (4,5),
    }

    return G, pos

def executar_a_estrela(G, origem, destino, pos):
    return nx.astar_path(G, origem, destino,
                         heuristic=lambda a,b: heuristica(a,b,pos),
                         weight='weight')

def executar_bfs(G, origem, destino):
    return nx.shortest_path(G, origem, destino)

def executar_dfs(G, origem, destino):
    return nx.shortest_path(G, origem, destino)