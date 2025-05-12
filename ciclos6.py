def tiene_ciclo(grafo):
    """
    Determina si un grafo no dirigido contiene al menos un ciclo.

    Complejidad temporal:
    O(V + E), donde V es el número de vértices y E el número de aristas.
    - Se visita cada nodo una sola vez (O(V)).
    - Se recorren todas las aristas una sola vez (O(E)).

    Complejidad espacial:
    O(V), ya que:
    - Se almacena un conjunto `visitado` con los vértices visitados.
    - La recursión de DFS puede ocupar hasta O(V) en la pila de llamadas.
    """

    visitado = set()  # Para registrar los nodos ya visitados

    def dfs(v, padre):
        """
        Función auxiliar recursiva para realizar DFS y detectar ciclos.

        Si encuentra un vecino visitado que no es el padre, detecta un ciclo.
        """
        visitado.add(v)
        for vecino in grafo[v]:
            if vecino not in visitado:
                if dfs(vecino, v):  # Llamada recursiva con el nodo actual como padre
                    return True
            elif vecino != padre:
                # Si el vecino ya fue visitado y no es el padre, hay un ciclo
                return True
        return False

    # Ejecutamos DFS desde cada nodo no visitado (por si el grafo no es conexo)
    for nodo in grafo:
        if nodo not in visitado:
            if dfs(nodo, None):
                return True

    return False


grafo = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 0]  # ciclo: 0-1-2-3-0
}

print(tiene_ciclo(grafo))  # Salida: True
