import heapq


def asignar_salones(actividades):
    """
    Asigna actividades a salones minimizando la cantidad de salones usados

    Complejidad temporal:
    - Ordenar actividades: O(n log n)
    - Por cada actividad hacemos operaciones push/pop en el heap: O(log k) donde k es el número de salones
    - Total: O(n log n), siendo n el número de actividades.

    Complejidad espacial:
    - O(n) para almacenar el heap, la asignación de actividades y las listas de salones.

    Justificación:
    - Ordenamos las actividades por su hora de inicio.
    - Utilizamos un min-heap para llevar seguimiento del tiempo de finalización de las actividades
      en los salones actuales, permitiendo reusar salones si la siguiente actividad empieza después
      del fin más temprano.
    - El heap mantiene los salones ordenados por la hora más temprana de disponibilidad, lo cual
      permite siempre asignar la próxima actividad al salón que se libera antes (si es posible).
    - Esto garantiza el uso mínimo de salones, equivalente al número máximo de actividades que se solapan.
    """

    #Ordeno actividades
    actividades_ordenadas = sorted(enumerate(actividades), key=lambda x: x[1][0])
    heap = []
    salones = {}
    asignaciones = {}
    siguiente_salon_id = 0

    # Iterar sobre las actividades ya ordenadas por inicio
    for id_actividad, (inicio, fin) in actividades_ordenadas:
        if heap and heap[0][0] <= inicio:
            # Reusar salón cuya actividad termina antes de que empiece la actual
            fin_anterior, salon_id = heapq.heappop(heap)
        else:
            # No hay salón libre, se debe crear uno nuevo
            salon_id = siguiente_salon_id
            siguiente_salon_id += 1
            salones[salon_id] = []

        # Asignar la actividad al salón seleccionado
        salones[salon_id].append((inicio, fin))
        asignaciones[id_actividad] = salon_id

        # Registrar el nuevo tiempo de finalización en el heap
        heapq.heappush(heap, (fin, salon_id))

    return salones, asignaciones


# Ejemplo de uso
if __name__ == "__main__":
    actividades = [(0, 30), (5, 10), (15, 20), (35, 50), (10, 15), (20, 40)]
    salones, asignaciones = asignar_salones(actividades)

    print("Asignación de actividades a salones:")
    for salon, acts in salones.items():
        print(f"Salón {salon}: {acts}")

    print("\nAsignaciones individuales:")
    for idx, salon in asignaciones.items():
        print(f"Actividad {idx} -> Salón {salon}")
