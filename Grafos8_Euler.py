from collections import defaultdict, deque

# Tiempo de ejecución: O(E)
# Uso de memoria: O(E + V)
# Justificación: Se recorre cada arista una sola vez, y se almacenan en estructuras auxiliares

def tiene_ciclo_euleriano(grafo):
    """
    Verifica si el grafo dirigido tiene un ciclo de Euler.
    :param grafo: Diccionario de adyacencia {u: [v1, v2, ...]}
    :return: True si existe un ciclo de Euler
    """
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for u in grafo:
        for v in grafo[u]:
            out_degree[u] += 1
            in_degree[v] += 1

    vertices = set(grafo.keys()) | set(in_degree.keys())
    for v in vertices:
        if in_degree[v] != out_degree[v]:
            return False
    return True


def recorrido_euleriano(grafo):
    """
    Encuentra un ciclo de Euler en un grafo dirigido si existe.
    :param grafo: Diccionario de adyacencia {u: [v1, v2, ...]}
    :return: Lista de nodos en orden de recorrido euleriano o None
    """
    if not tiene_ciclo_euleriano(grafo):
        return None

    grafo_copia = {u: deque(vs) for u, vs in grafo.items()}  # Copia con deque para O(1) pop
    circuito = []
    stack = []
    
    # Elegimos un vértice con al menos una arista saliente como inicio
    actual = next((v for v in grafo if grafo[v]), None)
    stack.append(actual)

    while stack:
        while grafo_copia[actual]:
            stack.append(actual)
            siguiente = grafo_copia[actual].popleft()
            actual = siguiente
        circuito.append(actual)
        actual = stack.pop()

    return circuito[::-1]  # Invertimos para obtener orden correcto


# Ejemplo de uso
if __name__ == "__main__":
    # Grafo dirigido representado como lista de adyacencia
    grafo = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }

    camino = recorrido_euleriano(grafo)
    if camino:
        print("Recorrido de Euler encontrado:")
        print(" -> ".join(camino))
    else:
        print("No existe un recorrido de Euler en este grafo.")
