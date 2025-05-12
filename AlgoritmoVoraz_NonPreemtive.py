# Tiempo de ejecución: O(n log n) debido al ordenamiento de las tareas
# Uso de memoria: O(n) para almacenar las tareas y sus tiempos
# Justificación: El ordenamiento domina el tiempo de ejecución. La memoria se usa para guardar la lista y variables auxiliares.

def minimizar_tiempo_promedio_non_preemptive(tiempos):
    """
    Minimiza el tiempo promedio de finalización bajo asignación no preemptiva.
    :param tiempos: Lista de tiempos de ejecución de las tareas [p1, p2, ..., pn]
    :return: Tiempo promedio de finalización
    """
    # Ordenamos los tiempos de menor a mayor (Shortest Job First)
    tiempos.sort()
    
    tiempo_actual = 0
    suma_finalizaciones = 0

    for p in tiempos:
        tiempo_actual += p
        suma_finalizaciones += tiempo_actual

    promedio = suma_finalizaciones / len(tiempos)
    return promedio


# Ejemplo de uso:
if __name__ == "__main__":
    tareas = [4, 2, 1, 3]  # Puedes cambiar los valores
    promedio = minimizar_tiempo_promedio_non_preemptive(tareas)
    print(f"Tiempo promedio de finalización (non-preemptive): {promedio}")
