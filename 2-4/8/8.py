from utils import write_output_2

def get_hashes(s, k, base=31, mod=10 ** 9 + 7):
    """Вычисление хешей всех подстрок длиной k для строки s."""
    n = len(s)
    hashes = {}
    hash_value = 0
    base_k = pow(base, k, mod)  # base^k % mod

    # Вычисляем хеш для первой подстроки длиной k
    for i in range(k):
        hash_value = (hash_value * base + ord(s[i])) % mod

    hashes[hash_value] = [0]  # добавляем индекс начала подстроки

    # Прокручиваем окно по строке и вычисляем хеши для подстрок
    for i in range(1, n - k + 1):
        hash_value = (hash_value * base + ord(s[i + k - 1]) - ord(s[i - 1]) * base_k) % mod
        if hash_value not in hashes:
            hashes[hash_value] = []
        hashes[hash_value].append(i)

    return hashes


def find_common_substring(s, t, k):
    """Проверка, есть ли общая подстрока длины k между строками s и t."""
    hashes_s = get_hashes(s, k)
    hashes_t = get_hashes(t, k)

    for hash_value in hashes_s:
        if hash_value in hashes_t:
            # Проверяем, совпадают ли подстроки
            for start_s in hashes_s[hash_value]:
                for start_t in hashes_t[hash_value]:
                    if s[start_s:start_s + k] == t[start_t:start_t + k]:
                        return start_s, start_t
    return None


def longest_common_substring(s, t):
    """Бинарный поиск длины наибольшей общей подстроки."""
    low, high = 0, min(len(s), len(t))
    best_length = 0
    best_pos_s = 0
    best_pos_t = 0

    while low <= high:
        mid = (low + high) // 2
        common_substr = find_common_substring(s, t, mid)

        if common_substr:
            best_length = mid
            best_pos_s, best_pos_t = common_substr
            low = mid + 1
        else:
            high = mid - 1

    return best_pos_s, best_pos_t, best_length


def process_input_output(input_file, output_file):
    # Чтение данных из input.txt
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()

    results = []

    # Проход по каждой строке
    for line in lines:
        s, t = line.split()  # разделение по пробелу
        pos_s, pos_t, length = longest_common_substring(s, t)
        results.append(f"{pos_s} {pos_t} {length}")

    # Запись результатов в output.txt с помощью функции из utils
    write_output_2(output_file, results)

# Пример вызова функции
process_input_output('input.txt', 'output.txt')
