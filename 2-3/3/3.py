from utils import write_output

def has_cycle(n, edges):
    # Строим граф
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)

    visited = [False] * n
    recursion_stack = [False] * n

    def dfs(v):
        visited[v] = True
        recursion_stack[v] = True

        for neighbor in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif recursion_stack[neighbor]:
                return True

        recursion_stack[v] = False
        return False

    for node in range(n):
        if not visited[node]:
            if dfs(node):
                return 1
    return 0

# Чтение данных
with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    edges = [tuple(map(int, line.split())) for line in f]

# Получаем результат
result = has_cycle(n, edges)

# Запись в файл с использованием функции из utils
write_output('output.txt', result)
