import heapq

# Tiempo de ejecución: O(n log n + T log n), T = tiempo total simulado
# Uso de memoria: O(n) para heap y almacenamiento de tareas
# Justificación: Se usa heap para acceder rápidamente a la tarea con menor tiempo restante

def minimizar_tiempo_promedio_preemptive(tareas):
    """
    Minimiza el tiempo promedio de finalización bajo asignación preemptive.
    :param tareas: Lista de tuplas (ri, pi) donde ri es el tiempo de llegada y pi el tiempo total de ejecución
    :return: Tiempo promedio de finalización
    """
    # Ordenamos tareas por tiempo de llegada
    tareas.sort()
    
    heap = []  # Min-heap por tiempo restante
    tiempo = 0
    i = 0
    n = len(tareas)
    terminaciones = []

    while i < n or heap:
        # Agregar tareas disponibles al heap
        while i < n and tareas[i][0] <= tiempo:
            ri, pi = tareas[i]
            heapq.heappush(heap, (pi, ri, i, pi))  # (tiempo restante, ri, id, tiempo original)
            i += 1

        if heap:
            tiempo_restante, ri, idx, tiempo_original = heapq.heappop(heap)
            tiempo += 1  # Ejecutamos por 1 unidad de tiempo
            tiempo_restante -= 1

            if tiempo_restante > 0:
                # Si no ha terminado, la volvemos a meter con tiempo restante actualizado
                heapq.heappush(heap, (tiempo_restante, ri, idx, tiempo_original))
            else:
                # Tarea completada
                terminaciones.append(tiempo)
        else:
            # No hay tareas disponibles, avanzamos el tiempo
            tiempo = tareas[i][0]

    promedio = sum(terminaciones) / n
    return promedio


# Ejemplo de uso
if __name__ == "__main__":
    tareas = [(0, 3), (1, 9), (2, 6)]  # (ri, pi)
    promedio = minimizar_tiempo_promedio_preemptive(tareas)
    print(f"Tiempo promedio de finalización (preemptive): {promedio}")
