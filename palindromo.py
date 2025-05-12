def longest_palindromic_subsequence(s):
    """
    Encuentra la subsecuencia palindrómica más larga en una cadena s.

    Complejidad temporal:
    - Llenar la tabla dp toma O(n²), donde n es la longitud de la cadena.
    - Reconstruir el palíndromo también toma O(n), pero está dominado por la fase anterior.
    - Total: O(n²)

    Complejidad espacial:
    - O(n²) para almacenar la tabla dp.

    Justificación:
    - Se utiliza programación dinámica para calcular la longitud del palíndromo más largo en cada subcadena s[i..j].
    - La tabla dp[i][j] guarda la longitud del palíndromo más largo en ese rango.
    - Se empieza desde subcadenas pequeñas (longitud 1) hasta subcadenas completas (longitud n).
    - Si los caracteres en los extremos coinciden, se suman al valor interno (dp[i+1][j-1] + 2).
    - Si no coinciden, se toma el máximo entre excluir el carácter izquierdo o el derecho.
    - Finalmente, se reconstruye el palíndromo usando la tabla dp, yendo desde los extremos hacia el centro.
    - Este enfoque garantiza encontrar la subsecuencia palindrómica más larga sin necesidad de evaluar todas las combinaciones posibles.
    """

    n = len(s)
    dp = [[0] * n for _ in range(n)]  # Tabla DP de tamaño n x n

    # Caso base: cada letra sola es un palíndromo de longitud 1
    for i in range(n):
        dp[i][i] = 1

    # Evaluar subcadenas de longitud 2 hasta n
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1  # Fin de la subcadena

            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2  # Dos letras iguales seguidas
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2  # Letras iguales en extremos
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])  # Excluir una letra

    # Reconstrucción del palíndromo
    i, j = 0, n - 1
    res = [""] * dp[0][n - 1]  # Espacio para el resultado
    start, end = 0, dp[0][n - 1] - 1  # Punteros para rellenar extremos

    while i <= j:
        if s[i] == s[j]:
            res[start] = s[i]
            res[end] = s[j]
            start += 1
            end -= 1
            i += 1
            j -= 1
        elif dp[i][j - 1] > dp[i + 1][j]:
            j -= 1  # Avanzar desde el lado derecho
        else:
            i += 1  # Avanzar desde el lado izquierdo

    return "".join(res)  # Convertir lista en string


# Ejemplo de uso
if _name_ == "_main_":
    cadena = "popocateptl"
    print("Entrada:", cadena)
    print("Palíndromo más largo como subsecuencia:", longest_palindromic_subsequence(cadena))
