import itertools

# Definición del grafo con conexiones de ida y vuelta
grafo = {
    'F': {'H': 9},
    'C': {'E': 1, 'B': 5, 'A': 5, 'F': 7},
    'A': {'B': 3, 'H': 10, 'C': 5},
    'H': {'B': 6, 'D': 14, 'G': 3, 'A': 10},
    'B': {'E': 4, 'D': 8, 'G': 6, 'A': 3, 'C': 5},
    'E': {'D': 12, 'G': 15, 'C': 1, 'B': 4},
    'G': {'C': 9, 'B': 6, 'H': 3},
    'D': {'A': 2, 'H': 14, 'B': 8, 'E': 12}
}

def calcular_distancia_camino(camino, grafo):
    distancia = 0
    for i in range(len(camino) - 1):
        origen = camino[i]
        destino = camino[i + 1]
        if destino in grafo[origen]:
            distancia += grafo[origen][destino]
        else:
            # Si no hay conexión directa entre los nodos, el camino no es válido
            return float('inf')
    return distancia

# Obtener todas las posibles permutaciones de los nodos
nodos = list(grafo.keys())
posibles_caminos = list(itertools.permutations(nodos))

# Almacenar los caminos válidos junto con sus distancias
caminos_validos = []
for camino in posibles_caminos:
    distancia = calcular_distancia_camino(camino, grafo)
    if distancia != float('inf'):
        caminos_validos.append((camino, distancia))

# Imprimir cada camino y su distancia
for i, (camino, distancia) in enumerate(caminos_validos, start=1):
    print(f"{i}: {camino} = {distancia}")

# Encontrar el camino más corto
camino_mas_corto, distancia_mas_corta = min(caminos_validos, key=lambda x: x[1])
print(f"\nEl camino más corto es: {camino_mas_corto} con una distancia de {distancia_mas_corta}")
