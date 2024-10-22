# utils.py
#2
def min_refills(d, m, stops):
    # Добавляем конечную точку в список заправок
    stops.append(d)
    n = len(stops)

    # Текущая позиция (начало пути)
    current_pos = 0
    # Количество заправок
    num_refills = 0

    # Пробегаем по заправкам
    for i in range(n):
        if stops[i] - current_pos > m:
            # Если не можем доехать до следующей заправки
            if i == 0 or stops[i] - stops[i - 1] > m:
                return -1
            # Заправляемся на предыдущей заправке
            current_pos = stops[i - 1]
            num_refills += 1

    # Финальная проверка: можем ли мы доехать до пункта назначения с последней заправки
    if d - current_pos > m:
        return -1

    return num_refills
#5
# utils.py

def max_number_of_prizes(n):
    prizes = []
    current_prize = 1

    while n > 0:
        if n - current_prize > current_prize:
            prizes.append(current_prize)
            n -= current_prize
            current_prize += 1
        else:
            prizes.append(n)
            n = 0

    return prizes
#10
# utils.py

def process_apples(n, s, apples):
    # Сортировка яблок по критерию (большее увеличение - меньшее уменьшение)
    apples.sort(key=lambda a: [-(a[1] - a[0]), a[0]])

    j = 0
    psbl = True
    order = []

    # Основной алгоритм для выбора порядка съедения яблок
    while psbl and j < n:
        found = False
        a = 0
        while a < n and not found:
            if s - apples[a][0] > 0 and apples[a][2] != 0:
                found = True
                s += apples[a][1] - apples[a][0]
                order.append(apples[a][2])
                apples[a][2] = 0  # Помечаем яблоко как съеденное
            a += 1
        psbl = found
        j += 1

    return order if psbl else -1
#16
# utils.py

INF = float('inf')

def tsp_with_path(n, a):
    n += 1  # Увеличиваем размерность для учета первой вершины

    # Инициализируем DP таблицу
    dp = [[INF] * (1 << n) for _ in range(n)]
    dp[0][0] = 0

    # Заполняем DP таблицу
    for mask in range(1 << n):
        for i in range(n):
            for j in range(n):
                if (mask & (1 << j)) > 0:
                    dp[i][mask] = min(dp[i][mask], dp[j][mask ^ (1 << j)] + a[i][j])

    # Восстанавливаем путь
    i = 0
    mask = (1 << n) - 1
    path = []

    while mask > 0:
        for j in range(n):
            if (mask & (1 << j)) > 0 and dp[i][mask] == dp[j][mask ^ (1 << j)] + a[i][j]:
                if j != 0:
                    path.append(j)
                i = j
                mask ^= (1 << j)
                break

    path.reverse()
    return dp[0][(1 << n) - 1], path  # Возвращаем минимальную стоимость и путь
#19
# utils.py

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


# utils.py

def write_output(filename, data):
    with open(filename, 'w') as f:
        f.write(str(data) + '\n')
# utils.py

def write_output_cicle(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(str(item) + '\n')
# utils.py

def write_output_2(filename, results):
    """Записывает результаты в файл."""
    with open(filename, 'w') as f:
        f.write("\n".join(results) + "\n")
# utils.py


