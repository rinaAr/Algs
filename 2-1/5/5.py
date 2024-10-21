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

# Чтение данных из файла input.txt
with open('input.txt', 'r') as f:
    n = int(f.readline().strip())

# Вызов функции
prizes = max_number_of_prizes(n)

# Запись результата в файл output.txt
with open('output.txt', 'w') as f:
    f.write(str(len(prizes)) + '\n')
    f.write(' '.join(map(str, prizes)) + '\n')
