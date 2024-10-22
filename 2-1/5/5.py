from utils import max_number_of_prizes

def main():
    # Чтение данных из файла input.txt
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())

    # Вызов функции
    prizes = max_number_of_prizes(n)

    # Запись результата в файл output.txt
    with open('output.txt', 'w') as f:
        f.write(str(len(prizes)) + '\n')
        f.write(' '.join(map(str, prizes)) + '\n')

if __name__ == "__main__":
    main()
