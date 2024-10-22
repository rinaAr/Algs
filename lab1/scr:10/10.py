from utils import process_apples

def main():
    # Чтение входных данных из файла input.txt
    with open('input.txt', 'r') as f:
        n, s = map(int, f.readline().strip().split())
        apples = []
        for i in range(n):
            a, b = map(int, f.readline().strip().split())
            apples.append([a, b, i + 1])

    # Вызов функции обработки
    result = process_apples(n, s, apples)

    # Запись результата в файл output.txt
    with open('output.txt', 'w') as f:
        if result != -1:
            f.write(' '.join(map(str, result)) + '\n')
        else:
            f.write('-1\n')

if __name__ == "__main__":
    main()
