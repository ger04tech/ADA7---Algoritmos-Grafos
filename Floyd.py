def floyd_warshall(dist):
    """ Implementa el algoritmo de Floyd-Warshall para encontrar la distancia mínima entre todas las parejas de nodos.
    
    Args:
    dist (list of list of int): Matriz de adyacencia donde dist[i][j] es la distancia directa desde el nodo i al nodo j,
                                o float('inf') si no hay conexión directa.
    
    Returns:
    list of list of int: Matriz de distancias mínimas entre todos los pares de nodos.
    """
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

inf = float('inf')
graph = [
    [0,   2, inf,   5],
    [inf, 0,   1, inf],
    [inf, inf, 0,   4],
    [3,   inf, inf, 0]
]

# Aplica el Floyd-Warshall al grafo.
distances = floyd_warshall(graph)


city_labels = ['A', 'B', 'C', 'D']
print("Matriz de distancias mínimas:")
for row in distances:
    print(row)

print("\nDistancias mínimas específicas:")
for i, origin in enumerate(city_labels):
    for j, destination in enumerate(city_labels):
        print(f"Distancia mínima de {origin} a {destination}: {distances[i][j]}")
