import math
from collections import defaultdict

def viterbi_max_path(graph, start, sequence):
    """
    Algoritmo de Viterbi (versión probabilística, parte B): encuentra el camino más probable
    en un grafo dirigido donde la secuencia de sonidos (etiquetas) debe coincidir exactamente con una dada.

    Complejidad temporal:
    - O(k * E), donde k es la longitud de la secuencia y E el número de aristas.
      Se procesan todas las aristas desde los nodos alcanzables en cada paso.

    Complejidad espacial:
    - O(k * V), donde V es el número de nodos. Se guarda la mejor probabilidad para cada nodo en cada paso.

    Justificación:
    - El algoritmo busca no solo un camino válido, sino el más probable.
    - Para cada paso i, se guarda en dp[i][v] la mejor probabilidad acumulada (en logaritmo) para llegar al nodo v.
    - Las probabilidades se manejan en logaritmo para evitar errores por precisión o subdesbordamiento con números muy pequeños.
    - En cada transición compatible con el símbolo actual, se acumula la probabilidad y se actualiza el camino si mejora.
    - Al final se elige el nodo final con mayor probabilidad y se reconstruye el camino desde los nodos padre almacenados.
    """

    n = len(sequence)
    dp = defaultdict(dict)  # dp[i][v] = (log(probabilidad acumulada), nodo padre)
    dp[0][start] = (0.0, None)  # log(1) = 0: empezamos con probabilidad 1 en el nodo inicial

    # Procesamos cada símbolo de la secuencia
    for i in range(n):
        current_symbol = sequence[i]
        for u in dp[i]:  # Para cada nodo alcanzado en el paso anterior
            curr_log_prob, _ = dp[i][u]
            for v, sigma, prob in graph.get(u, []):  # Transiciones desde u
                if sigma == current_symbol:
                    # Acumulamos la probabilidad usando logaritmos
                    new_log_prob = curr_log_prob + math.log(prob)
                    # Si es mejor que la anterior, actualizamos
                    if v not in dp[i + 1] or new_log_prob > dp[i + 1][v][0]:
                        dp[i + 1][v] = (new_log_prob, u)

    # Si no hay nodos alcanzados al final, no hay solución
    if not dp[n]:
        return "No path found"

    # Elegimos el nodo final con mayor probabilidad acumulada
    end = max(dp[n], key=lambda x: dp[n][x][0])
    path = [end]

    # Reconstrucción del camino óptimo desde los nodos padre
    for i in range(n, 0, -1):
        end = dp[i][end][1]
        path.append(end)

    return path[::-1]  # Invertimos el camino para devolverlo de inicio a fin


# Ejemplo de uso
graph_b = {
    'A': [('B', 'a', 0.5), ('C', 'b', 0.5)],
    'B': [('D', 'b', 0.6)],
    'C': [('D', 'a', 0.9)],
    'D': []
}

# Buscar camino más probable para la secuencia ['a', 'b']
print(viterbi_max_path(graph_b, 'A', ['a', 'b']))  # Resultado esperado: ['A', 'B', 'D']
