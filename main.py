from buscar import *
from clustering import *

G, pos = criar_grafo()

print("A*:", executar_a_estrela(G, "Centro", "D", pos))
print("BFS:", executar_bfs(G, "Centro", "D"))
print("DFS:", executar_dfs(G, "Centro", "D"))

df_clusters = aplicar_kmeans("data/entregas.csv", 2)
print(df_clusters)