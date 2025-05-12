def longest_palindromic_subsequence(s):
    """
    Encuentra la subsecuencia palindrómica más larga en una cadena s.

    Tiempo: O(n²)  |  Espacio: O(n²)

    Se utiliza programación dinámica. La tabla dp[i][j] guarda la longitud
    del palíndromo más largo dentro de s[i..j].
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1  # Cada carácter por sí solo es un palíndromo

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # Reconstrucción del palíndromo
    i, j = 0, n - 1
    res = [""] * dp[0][n - 1]
    start, end = 0, dp[0][n - 1] - 1

    while i <= j:
        if s[i] == s[j]:
            res[start] = s[i]
            res[end] = s[j]
            start += 1
            end -= 1
            i += 1
            j -= 1
        elif dp[i][j - 1] > dp[i + 1][j]:
            j -= 1
        else:
            i += 1

    return "".join(res)


# 🧪 Caso de prueba
cadena = "popocateptl"
print("Entrada:", cadena)
print("Palíndromo más largo como subsecuencia:", longest_palindromic_subsequence(cadena))
# Esperado: "carac"
