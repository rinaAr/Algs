def hash_prefixes(s):
    """Вычисляет хеш-значения префиксов строки s."""
    p = 31  # простое число для хеширования
    m = 10 ** 9 + 9  # модуль
    n = len(s)
    hash_values = [0] * (n + 1)
    p_pow = [1] * (n + 1)

    for i in range(n):
        hash_values[i + 1] = (hash_values[i] * p + ord(s[i])) % m
        p_pow[i + 1] = (p_pow[i] * p) % m

    return hash_values, p_pow


def count_mismatches(t, p, start, k):
    """Считает количество несовпадений между p и подстрокой t[start:start + len(p)]."""
    mismatches = 0
    for i in range(len(p)):
        if t[start + i] != p[i]:
            mismatches += 1
            if mismatches > k:
                return mismatches
    return mismatches


def process_input_output(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()

    results = []

    for line in lines:
        k, t, p = line.split()
        k = int(k)
        t_length = len(t)
        p_length = len(p)

        positions = []

        # Перебираем все возможные позиции в t
        for i in range(t_length - p_length + 1):
            mismatches = count_mismatches(t, p, i, k)  # Передаем k как аргумент
            if mismatches <= k:
                positions.append(i)

        results.append(f"{len(positions)} {' '.join(map(str, positions))}")

    # Записываем результаты в output.txt
    with open(output_file, 'w') as f:
        f.write("\n".join(results))


# Вызов функции для обработки
process_input_output('input.txt', 'output.txt')
