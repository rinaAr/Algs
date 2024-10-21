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


# Чтение данных из файла input.txt
with open('input.txt', 'r') as f:
    d = int(f.readline().strip())  # Расстояние до пункта назначения
    m = int(f.readline().strip())  # Максимальное расстояние на полном баке
    n = int(f.readline().strip())  # Количество заправок
    stops = list(map(int, f.readline().strip().split()))  # Расстояния до заправок

# Вызов функции
result = min_refills(d, m, stops)

# Запись результата в файл output.txt
with open('output.txt', 'w') as f:
    f.write(str(result) + '\n')
