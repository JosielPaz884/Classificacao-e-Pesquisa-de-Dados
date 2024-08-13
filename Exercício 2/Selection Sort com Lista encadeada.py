class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def selectionSort(self):
        if not self.head:
            return

        current = self.head
        while current:
            minNode = current
            nextNode = current.next
            while nextNode:
                if nextNode.data < minNode.data:
                    minNode = nextNode
                nextNode = nextNode.next
            if minNode != current:
                current.data, minNode.data = minNode.data, current.data
            current = current.next

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    array = LinkedList()
    n = int(input("Digite a quantidade de elementos:"))
    for i in range(n):
        element = int(input("Digite o elemento:"))
        array.insert(element)

    print("-----------------")
    print("Lista original:")
    array.printList()
    array.selectionSort()
    print("-----------------")
    print("Lista ordenada:")
    array.printList()

if __name__ == "__main__":
    main()
