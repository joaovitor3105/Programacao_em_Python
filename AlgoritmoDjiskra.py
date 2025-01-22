import numpy as np

def dijkstra(grafo, origem):
    n_vertices = len(grafo)
    distancias = np.full(n_vertices, np.inf)
    distancias[origem] = 0
    visitados = np.zeros(n_vertices, dtype=bool)
    anterior = np.full(n_vertices, -1, dtype=int)
    
    for _ in range(n_vertices):
        nao_visitados = np.where(~visitados)[0]
        if len(nao_visitados) > 0:
            u = nao_visitados[np.argmin(distancias[nao_visitados])]
        else:
            break
            
        visitados[u] = True
        
        for v in range(n_vertices):
            if grafo[u][v] > 0 and not visitados[v]:
                nova_distancia = distancias[u] + grafo[u][v]
                if nova_distancia < distancias[v]:
                    distancias[v] = nova_distancia
                    anterior[v] = u
    
    return distancias, anterior

def recuperar_caminho(anterior, origem, destino):
    caminho = []
    atual = destino
    
    while atual != -1:
        caminho.insert(0, int(atual))
        atual = anterior[atual]
        
    return caminho if caminho[0] == origem else []

grafo = np.array([
    [0, 10, 0, 30, 100],
    [10, 0, 50, 0, 0],
    [0, 50, 0, 20, 10],
    [30, 0, 20, 0, 60],
    [100, 0, 10, 60, 0]
])

origem = 0
distancias, anterior = dijkstra(grafo, origem)

print(f"\nDistâncias mínimas a partir do nó {origem}:")
for i, dist in enumerate(distancias):
    caminho = recuperar_caminho(anterior, origem, i)
    print(f"Até o nó {i}: {dist:.1f} (Caminho: {caminho})")
