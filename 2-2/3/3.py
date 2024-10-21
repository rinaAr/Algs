class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def find_min_greater_than(self, key):
        return self._find_min_greater_than(self.root, key, None)

    def _find_min_greater_than(self, node, key, successor):
        if node is None:
            return successor

        if node.val <= key:
            return self._find_min_greater_than(node.right, key, successor)
        else:
            return self._find_min_greater_than(node.left, key, node.val)

# Чтение данных и выполнение запросов
bst = BinarySearchTree()
results = []

with open('input.txt', 'r') as f:
    for line in f:
        command = line.strip().split()
        if command[0] == '+':
            x = int(command[1])
            bst.insert(x)
        elif command[0] == '>':
            x = int(command[1])
            result = bst.find_min_greater_than(x)
            results.append(result if result is not None else 0)

# Запись результата в файл
with open('output.txt', 'w') as f:
    for result in results:
        f.write(str(result) + '\n')
