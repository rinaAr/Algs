class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left_index = None
        self.right_index = None


def calculate_balance_and_height(node, nodes):
    if node is None:
        return 0, 0  # высота и баланс для пустого узла

    # Рекурсивно вычисляем высоты левого и правого поддерева
    left_height, _ = calculate_balance_and_height(nodes[node.left_index - 1], nodes) if node.left_index else (0, 0)
    right_height, _ = calculate_balance_and_height(nodes[node.right_index - 1], nodes) if node.right_index else (0, 0)

    # Вычисляем баланс узла
    balance = right_height - left_height

    # Возвращаем высоту и баланс
    return max(left_height, right_height) + 1, balance


# Чтение данных
nodes = []

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())

    for _ in range(N):
        K, L, R = map(int, f.readline().strip().split())
        node = TreeNode(K)
        node.left_index = L
        node.right_index = R
        nodes.append(node)

# Вычисляем баланс для каждого узла и сохраняем его
balances = []
for i in range(N):
    _, balance = calculate_balance_and_height(nodes[i], nodes)
    balances.append(balance)

# Запись результата в файл
with open('output.txt', 'w') as f:
    for balance in balances:
        f.write(str(balance) + '\n')
