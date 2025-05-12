import math
from collections import defaultdict


def viterbi_max_path(graph, start, sequence):
    """
    Algoritmo de Viterbi (parte b): busca el camino más probable en el grafo G
    cuya secuencia de sonidos coincida con la dada.

    Complejidad temporal: O(k * E)
    Complejidad espacial: O(k * V)

    Se almacena la probabilidad acumulada en forma logarítmica para evitar errores numéricos,
    así como el nodo padre para reconstruir el camino óptimo.
    """
    n = len(sequence)
    dp = defaultdict(dict)  # dp[i][v] = (log(probabilidad acumulada), nodo padre)
    dp[0][start] = (0.0, None)  # log(1) = 0: probabilidad inicial en el nodo de inicio

    for i in range(n):
        current_symbol = sequence[i]
        for u in dp[i]:
            curr_log_prob, _ = dp[i][u]
            for v, sigma, prob in graph.get(u, []):
                if sigma == current_symbol:
                    new_log_prob = curr_log_prob + math.log(prob)
                    if v not in dp[i + 1] or new_log_prob > dp[i + 1][v][0]:
                        dp[i + 1][v] = (new_log_prob, u)

    if not dp[n]:
        return "No path found"

    # Elegimos el nodo final con mayor probabilidad
    end = max(dp[n], key=lambda x: dp[n][x][0])
    path = [end]

    for i in range(n, 0, -1):
        end = dp[i][end][1]
        path.append(end)

    return path[::-1]

graph_b = {
    'A': [('B', 'a', 0.5), ('C', 'b', 0.5)],
    'B': [('D', 'b', 0.6)],
    'C': [('D', 'a', 0.9)],
    'D': []
}
print(viterbi_max_path(graph_b, 'A', ['a', 'b']))  # Ej: ['A', 'B', 'D']