class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class ABB:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insertRec(self.root, key)

    def insertRec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insertRec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insertRec(node.right, key)

    def search(self, key):
        return self.searchRec(self.root, key)

    def searchRec(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self.searchRec(node.left, key)
        return self.searchRec(node.right, key)

    def delete(self, key):
        self.root = self.deleteRec(self.root, key)

    def deleteRec(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self.deleteRec(node.left, key)
        elif key > node.val:
            node.right = self.deleteRec(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.minValueNode(node.right)
            node.val = temp.val
            node.right = self.deleteRec(node.right, temp.val)
        return node

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def printPreOrder(self, node):
        if node:
            print(node.val, end=' ')
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)

    def printPostOrder(self, node):
        if node:
            self.printPostOrder(node.left)
            self.printPostOrder(node.right)
            print(node.val, end=' ')

    def printInOrder(self, node):
        if node:
            self.printInOrder(node.left)
            print(node.val, end=' ')
            self.printInOrder(node.right)

# Exemplo de uso
abb = ABB()
abb.insert(50)
abb.insert(30)
abb.insert(70)
abb.insert(20)
abb.insert(40)
abb.insert(60)
abb.insert(80)

print("Impressão em pré-ordem:")
abb.printPreOrder(abb.root)
print("\nImpressão em ordem simétrica:")
abb.printInOrder(abb.root)
print("\nImpressão em pós-ordem:")
abb.printPostOrder(abb.root)

abb.delete(20)
print("\nApós deletar 20, impressão em ordem simétrica:")
abb.printInOrder(abb.root)

foundNode = abb.search(30)
print("\nBusca por 30:", "Encontrado" if foundNode else "Não encontrado")
