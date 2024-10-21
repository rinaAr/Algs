def rabin_karp(P, T):
    p_len = len(P)
    t_len = len(T)
    base = 256
    mod = 10**9 + 7

    def hash_func(s, length):
        h = 0
        for i in range(length):
            h = (h * base + ord(s[i])) % mod
        return h

    # Вычисляем хэш паттерна P и начального окна T
    p_hash = hash_func(P, p_len)
    t_hash = hash_func(T, p_len)

    # Препроцессинг для быстрого пересчета хэша при сдвиге окна
    h = pow(base, p_len - 1, mod)

    result = []
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:  # Возможное совпадение
            if T[i:i + p_len] == P:
                result.append(i + 1)  # Добавляем индекс (начиная с 1)
        if i < t_len - p_len:
            t_hash = (t_hash - ord(T[i]) * h) % mod
            t_hash = (t_hash * base + ord(T[i + p_len])) % mod
            t_hash = (t_hash + mod) % mod  # Избегаем отрицательных хэшей

    return result

# Чтение данных из файлов
with open('input.txt', 'r') as file:
    P = file.readline().strip()
    T = file.readline().strip()

# Вызов функции
indices = rabin_karp(P, T)

# Запись результатов в файл
with open('output.txt', 'w') as file:
    file.write(f"{len(indices)}\n")
    file.write(" ".join(map(str, indices)) + "\n")
