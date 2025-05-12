from collections import defaultdict

def viterbi_find_path(graph, start, sequence):
    """
    Algoritmo de Viterbi (versión determinista, parte A): encuentra un camino en un grafo dirigido
    donde la concatenación de las etiquetas de las aristas sea exactamente igual a una secuencia dada.

    Complejidad temporal:
    - O(k * E), donde k es la longitud de la secuencia y E el número de aristas del grafo.
      En cada paso i (para cada símbolo), se recorren todos los nodos alcanzables y sus transiciones.

    Complejidad espacial:
    - O(k * V), siendo V el número de nodos (vértices) del grafo.
      Se guarda un diccionario dp que indica desde qué nodo se llegó a otro en cada paso.

    Justificación:
    - Se aplica programación dinámica para evitar recorrer caminos repetidos.
    - La idea es simular, paso a paso, los símbolos de la secuencia,
      registrando qué nodos son alcanzables en ese paso exacto y desde dónde.
    - Al final, si se logra alcanzar algún nodo en el último paso (longitud de la secuencia),
      se reconstruye el camino usando los "nodos padre" registrados en cada paso.
    - Esta técnica evita recorrer caminos inválidos y permite resolver el problema en tiempo eficiente,
      aún cuando el grafo es grande.
    """

    n = len(sequence)
    dp = defaultdict(dict)  # dp[i][v] = nodo padre desde el cual se llegó a v en paso i
    dp[0][start] = None     # En el paso 0, solo se puede estar en el nodo inicial

    # Por cada símbolo de la secuencia (paso i)
    for i in range(n):
        current_symbol = sequence[i]
        for u in dp[i]:  # Por cada nodo alcanzado en el paso anterior
            for v, sigma in graph.get(u, []):  # Por cada transición saliente desde u
                if sigma == current_symbol:
                    # Solo registramos v si aún no se había alcanzado en el paso i+1
                    if v not in dp[i + 1]:
                        dp[i + 1][v] = u  # Guardamos quién llevó a v en ese paso

    # Si no se alcanzó ningún nodo al final de la secuencia, no hay solución
    if not dp[n]:
        return "No path found"

    # Reconstrucción del camino desde cualquier nodo final válido
    end = next(iter(dp[n]))  # Tomamos el primero que encontramos
    path = [end]
    for i in range(n, 0, -1):
        end = dp[i][end]
        path.append(end)

    return path[::-1]  # Invertimos para tener el camino de inicio a fin


# Ejemplo de uso con grafo dirigido
graph_a = {
    'A': [('B', 'a'), ('C', 'b')],
    'B': [('D', 'b')],
    'C': [('D', 'a')],
    'D': []
}

# Buscar camino que siga la secuencia ['a', 'b']
print(viterbi_find_path(graph_a, 'A', ['a', 'b']))  # Resultado esperado: ['A', 'B', 'D']
