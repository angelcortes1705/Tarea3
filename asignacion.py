from bisect import bisect_right


def compute_previous(activities):
    activities.sort(key=lambda x: x[1])
    prev = []
    for i in range(len(activities)):
        j = bisect_right([a[1] for a in activities], activities[i][0]) - 1
        prev.append(j)
    return prev


def weighted_interval_scheduling(activities):
    """
    Asignación óptima de actividades no traslapadas con valor máximo (un solo salón).

    Tiempo: O(n log n)  |  Espacio: O(n²)
    """
    n = len(activities)
    prev = compute_previous(activities)
    dp = [0] * (n + 1)
    selected = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        act = activities[i - 1]
        incl_val = act[2] + dp[prev[i - 1] + 1]
        excl_val = dp[i - 1]
        if incl_val > excl_val:
            dp[i] = incl_val
            selected[i] = selected[prev[i - 1] + 1] + [act]
        else:
            dp[i] = excl_val
            selected[i] = selected[i - 1]

    return dp[n], selected[n]


def max_dual_room_value(activities):
    """
    Prueba todas las combinaciones de actividades en dos salones y
    retorna la asignación de máximo valor posible.

    Tiempo: O(2^n * n log n)  |  Espacio: O(n²)
    """
    best = 0
    best_pair = ([], [])
    n = len(activities)

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
# Cada actividad es (inicio, fin, valor)
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
