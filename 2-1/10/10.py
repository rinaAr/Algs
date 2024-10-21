# Чтение входных данных из файла input.txt
with open('input.txt', 'r') as f:
    n, s = map(int, f.readline().strip().split())
    apples = []
    for i in range(n):
        a, b = map(int, f.readline().strip().split())
        apples.append([a, b, i + 1])

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

# Запись результата в файл output.txt
with open('output.txt', 'w') as f:
    if psbl:
        f.write(' '.join(map(str, order)) + '\n')
    else:
        f.write('-1\n')
