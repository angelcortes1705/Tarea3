from bisect import bisect_right

def compute_previous(activities):
    """
    Para cada actividad, encuentra el índice de la última que no se traslapa con ella.

    Complejidad: O(n log n)
    - Ordenamos las actividades por hora de finalización.
    - Luego, para cada actividad usamos búsqueda binaria para encontrar
      la última que termina antes de que inicie esta.
    """
    activities.sort(key=lambda x: x[1])  # Ordenamos por hora de fin
    prev = []
    for i in range(len(activities)):
        j = bisect_right([a[1] for a in activities], activities[i][0]) - 1
        prev.append(j)
    return prev


def weighted_interval_scheduling(activities):
    """
    Encuentra el subconjunto de actividades no traslapadas con valor total máximo
    usando programación dinámica. Solo se usa un salón.

    Complejidad temporal:
    - O(n log n) para ordenar y buscar actividades compatibles.
    - O(n) para calcular el valor óptimo.
    - Total: O(n log n)

    Complejidad espacial:
    - O(n) para la tabla de programación dinámica y la selección de actividades.

    Justificación:
    - Se modela el problema como una variante del clásico problema del "knapsack".
    - Cada actividad tiene inicio, fin y valor.
    - Usamos dp[i] para guardar el valor óptimo usando las primeras i actividades.
    - Se decide si incluir o excluir cada actividad según cuál da más valor.
    """
    n = len(activities)
    prev = compute_previous(activities)
    dp = [0] * (n + 1)
    selected = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        act = activities[i - 1]
        incl_val = act[2] + dp[prev[i - 1] + 1]  # Valor si se incluye esta
        excl_val = dp[i - 1]                    # Valor si se excluye esta
        if incl_val > excl_val:
            dp[i] = incl_val
            selected[i] = selected[prev[i - 1] + 1] + [act]
        else:
            dp[i] = excl_val
            selected[i] = selected[i - 1]

    return dp[n], selected[n]


def max_dual_room_value(activities):
    """
    Divide las actividades entre dos salones para maximizar el valor total.

    Complejidad temporal:
    - O(2^n * n log n): se prueban todas las particiones posibles de actividades (2^n),
      y por cada partición se calcula la solución óptima para cada conjunto con programación dinámica.

    Complejidad espacial:
    - O(n²): por la duplicación de resultados parciales y almacenamiento de soluciones intermedias.

    Justificación:
    - Se usa fuerza bruta para probar todas las formas de dividir las actividades en dos conjuntos.
    - Para cada subconjunto, se aplica programación dinámica (Weighted Interval Scheduling).
    - Se guarda la mejor combinación posible de actividades entre ambos salones.
    - El resultado es el mayor valor total posible sin traslapes dentro de cada salón.
    """
    best = 0
    best_pair = ([], [])
    n = len(activities)

    # Probar todas las formas de dividir las actividades
    for mask in range(1 << n):
        A1, A2 = [], []
        for i in range(n):
            if (mask >> i) & 1:
                A1.append(activities[i])
            else:
                A2.append(activities[i])

        val1, set1 = weighted_interval_scheduling(A1)
        val2, set2 = weighted_interval_scheduling(A2)
        if val1 + val2 > best:
            best = val1 + val2
            best_pair = (set1, set2)

    return best, best_pair


# 🧪 Caso de prueba
# Cada actividad tiene: (hora de inicio, hora de fin, valor)
if _name_ == "_main_":
    actividades = [
        (1, 4, 10),
        (3, 5, 20),
        (0, 6, 50),
        (5, 7, 30),
        (3, 9, 40),
        (5, 9, 25),
        (6, 10, 60),
        (8, 11, 55),
    ]

    valor_max, (salon1, salon2) = max_dual_room_value(actividades)
    print("Valor total máximo:", valor_max)
    print("Actividades en salón 1:", salon1)
    print("Actividades en salón 2:", salon2)
