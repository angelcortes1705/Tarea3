import math
import heapq
from collections import defaultdict

def camino_mas_confiable(grafo, inicio, fin):
    """
    Encuentra el camino más confiable (máximo producto de probabilidades) entre dos nodos en un grafo dirigido.

    Complejidad temporal:
    - O((V + E) log V), similar a Dijkstra usando heap.

    Complejidad espacial:
    - O(V), para distancias y predecesores.

    Justificación:
    - Usamos logaritmos negativos para transformar multiplicación en suma.
    - Aplicamos Dijkstra para minimizar el costo total de -log(probabilidad),
      lo cual equivale a maximizar el producto original de probabilidades.
    """

    heap = [(-0.0, inicio, [])]  # (neg_log_prob, nodo_actual, camino)
    visitado = set()

    while heap:
        neg_log_prob, nodo, camino = heapq.heappop(heap)
        if nodo in visitado:
            continue
        visitado.add(nodo)
        camino = camino + [nodo]

        if nodo == fin:
            prob_total = math.exp(-neg_log_prob)  # Convertimos log negativo a probabilidad real
            return prob_total, camino

        for vecino, prob in grafo[nodo]:
            if prob > 0:
                nuevo_costo = neg_log_prob - math.log(prob)
                heapq.heappush(heap, (nuevo_costo, vecino, camino))

    return 0.0, "No hay camino confiable"


# Ejemplo de uso
if __name__ == "_main_":
    grafo = {
    'A': [('B', 0.9), ('C', 0.5)],
    'B': [('D', 0.7), ('E', 0.6)],
    'C': [('E', 0.9)],
    'D': [('F', 0.8)],
    'E': [('F', 0.9)],
    'F': []
    }

    prob, camino = camino_mas_confiable(grafo, 'A', 'F')
    print("Probabilidad máxima:", prob)
    print("Camino más confiable:", camino)