from utils import min_refills, write_output

def main():
    # Чтение данных из файла input.txt
    with open('input.txt', 'r') as f:
        d = int(f.readline().strip())  # Расстояние до пункта назначения
        m = int(f.readline().strip())  # Максимальное расстояние на полном баке
        n = int(f.readline().strip())  # Количество заправок
        stops = list(map(int, f.readline().strip().split()))  # Расстояния до заправок

    # Вызов функции
    data = min_refills(d, m, stops)

    # Запись результата в файл с помощью функции из utils
    write_output('output.txt', data)

if __name__ == "__main__":
    main()
