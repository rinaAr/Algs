from utils import tsp_with_path

def main():
    # Чтение данных из файла input.txt
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        n = int(infile.readline().strip())

        # Чтение матрицы смежности
        a = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            a[i][1:n + 1] = list(map(int, infile.readline().strip().split()))

        # Вызов функции tsp_with_path
        min_cost, path = tsp_with_path(n, a)

        # Запись минимальной стоимости в файл output.txt
        outfile.write(str(min_cost) + '\n')

        # Запись пути в файл output.txt
        outfile.write(' '.join(map(str, path)) + '\n')

if __name__ == "__main__":
    main()
