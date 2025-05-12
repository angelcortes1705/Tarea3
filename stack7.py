def dfs_iterativa(grafo, inicio):
    """
    Realiza una búsqueda en profundidad (DFS) no recursiva a partir del nodo 'inicio'.

    Complejidad temporal:
    O(V + E), donde V es el número de vértices y E el número de aristas.
    - Cada nodo se visita una vez.
    - Cada arista se examina una vez en grafos no dirigidos.

    Complejidad espacial:
    O(V), ya que:
    - Se mantiene un conjunto de nodos visitados.
    - El stack puede almacenar hasta V nodos en el peor caso.

    Explicación:
    En lugar de usar llamadas recursivas del sistema, utilizamos un stack
    para controlar el flujo del algoritmo, simulando el comportamiento recursivo.
    """
    visitado = set()         # Set para registrar nodos visitados
    stack = [inicio]         # Stack inicializado con el nodo de inicio
    orden_visita = []        # Lista para registrar el orden de visita

    while stack:
        nodo = stack.pop()   # Tomar el último nodo agregado
        if nodo not in visitado:
            visitado.add(nodo)
            orden_visita.append(nodo)
            # Añadir vecinos al stack (en orden inverso)
            for vecino in reversed(grafo[nodo]):
                if vecino not in visitado:
                    stack.append(vecino)

    return orden_visita


grafo = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1, 4],
    4: [3]
}

print(dfs_iterativa(grafo, 0))  # Salida esperada: [0, 2, 1, 3, 4] (puede variar por el orden de vecinos)
