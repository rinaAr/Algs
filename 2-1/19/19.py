def matrix_chain_order(dimensions):
    n = len(dimensions) - 1  # количество матриц
    m = [[0] * n for _ in range(n)]  # m[i][j] - минимальное количество операций
    s = [[0] * n for _ in range(n)]  # s[i][j] - индекс, где происходит разделение

    for length in range(2, n + 1):  # длина цепочки
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        return f"A{i + 1}"
    else:
        return f"({print_optimal_parens(s, i, s[i][j])}{print_optimal_parens(s, s[i][j] + 1, j)})"


def main():
    # Чтение входных данных
    with open("input.txt", "r") as file:
        n = int(file.readline().strip())
        dimensions = []
        for _ in range(n):
            a, b = map(int, file.readline().strip().split())
            dimensions.append(a)  # количество строк
            dimensions.append(b)  # количество столбцов

    dimensions = list(dict.fromkeys(dimensions))  # Удаление дубликатов, чтобы получить размеры
    m, s = matrix_chain_order(dimensions)

    # Вывод оптимальной расстановки
    optimal_parenthesization = print_optimal_parens(s, 0, len(dimensions) - 2)

    with open("output.txt", "w") as file:
        file.write(optimal_parenthesization + "\n")


if __name__ == "__main__":
    main()
