from utils import write_output

def dfs(grid, visited, x, y):
    # Направления для движения: вниз, вверх, вправо, влево
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    stack = [(x, y)]  # Стек для DFS

    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # Проверка границ и посещенности
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and \
               grid[nx][ny] == '#' and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))

# Чтение данных
with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    grid = [list(f.readline().strip()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
beds_count = 0

# Обход по участку
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#' and not visited[i][j]:  # Если нашли грядку
            visited[i][j] = True
            dfs(grid, visited, i, j)  # Запускаем DFS
            beds_count += 1  # Увеличиваем счётчик грядок

# Запись результата
write_output('output.txt', beds_count)
