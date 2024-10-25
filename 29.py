# Binary Search Tree-ийн бүтэц
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Утга нэмэх функц (insert)
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    # Утга хайх функц (search)
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

    # Хамгийн бага утгыг олох функц (find_min)
    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    # Хамгийн их утгыг олох функц (find_max)
    def find_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

# Жишээ хэрэглээ
bst = BinarySearchTree()


values = [20, 9, 25, 5, 12, 15, 30]
for v in values:
    bst.insert(v)


print("Minimum value:", bst.find_min()) 
print("Maximum value:", bst.find_max())


print("Search 12:", "Found" if bst.search(12) else "Not Found")
print("Search 18:", "Found" if bst.search(18) else "Not Found")
