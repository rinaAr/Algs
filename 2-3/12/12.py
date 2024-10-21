def check_path(n, corridors, path):
    # Проверка: путь должен содержать хотя бы две комнаты
    if len(path) < 1:  # Путь может быть пустым
        return 1  # Если путь пустой, остается в комнате 1

    # Строим граф как список смежности
    graph = [{} for _ in range(n)]
    for u, v, color in corridors:
        if color not in graph[u - 1]:
            graph[u - 1][color] = []
        if color not in graph[v - 1]:
            graph[v - 1][color] = []
        graph[u - 1][color].append(v - 1)
        graph[v - 1][color].append(u - 1)

    current_room = 0  # Начинаем с комнаты 1 (индекс 0)

    # Проверяем путь
    for color in path:
        if color in graph[current_room]:  # Если есть коридор нужного цвета
            # Переходим в первую комнату по этому цвету (можно улучшить для выбора конкретной комнаты)
            current_room = graph[current_room][color][0]  # Переход в первую подходящую комнату
        else:
            return "INCORRECT"

    return current_room + 1  # Возвращаем номер комнаты (индекс + 1)

# Чтение данных
with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    corridors = [tuple(map(int, f.readline().split())) for _ in range(m)]
    k = int(f.readline().strip())
    path = list(map(int, f.readline().split())) if k > 0 else []

# Проверка пути
result = check_path(n, corridors, path)

# Запись в файл
with open('output.txt', 'w') as f:
    if result == "INCORRECT":
        f.write("INCORRECT\n")
    else:
        f.write(str(result) + '\n')
