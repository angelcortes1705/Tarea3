from collections import defaultdict


def viterbi_find_path(graph, start, sequence):
    """
    Algoritmo de Viterbi (parte a): busca un camino en el grafo G cuya concatenación de sonidos
    sea igual a la secuencia dada.

    Complejidad temporal: O(k * E), donde k es la longitud de la secuencia y E es el número de aristas.
    Complejidad espacial: O(k * V), donde V es el número de vértices.

    Se usa programación dinámica para almacenar los nodos alcanzables en cada paso i,
    guardando para cada uno el nodo padre para reconstruir el camino.
    """
    n = len(sequence)
    dp = defaultdict(dict)  # dp[i][v] = nodo padre desde el cual se llegó a v en paso i
    dp[0][start] = None  # En el paso 0, solo se puede estar en el nodo inicial

    for i in range(n):
        current_symbol = sequence[i]
        for u in dp[i]:
            for v, sigma in graph.get(u, []):
                if sigma == current_symbol:
                    if v not in dp[i + 1]:
                        dp[i + 1][v] = u

    if not dp[n]:
        return "No path found"

    # Reconstrucción del camino desde el último nodo alcanzado
    end = next(iter(dp[n]))  # Tomamos cualquier nodo final válido
    path = [end]
    for i in range(n, 0, -1):
        end = dp[i][end]
        path.append(end)

    return path[::-1]  # Regresamos el camino de inicio a fin

# Grafo para pruebas (formato para parte a)
graph_a = {
    'A': [('B', 'a'), ('C', 'b')],
    'B': [('D', 'b')],
    'C': [('D', 'a')],
    'D': []
}
print(viterbi_find_path(graph_a, 'A', ['a', 'b']))  # Ej: ['A', 'B', 'D']