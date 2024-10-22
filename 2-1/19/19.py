from utils import matrix_chain_order, print_optimal_parens, write_output

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
    data = print_optimal_parens(s, 0, len(dimensions) - 2)

    # Запись результата в файл с помощью функции из utils
    write_output("output.txt", data)

if __name__ == "__main__":
    main()
