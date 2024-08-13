class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def insertionSort(self):
        sortedHead = None
        current = self.head
        while current:
            temp = current.next
            if not sortedHead or current.data < sortedHead.data:
                current.next = sortedHead
                sortedHead = current
            else:
                sortedNode = sortedHead
                while sortedNode.next and current.data > sortedNode.next.data:
                    sortedNode = sortedNode.next
                current.next = sortedNode.next
                sortedNode.next = current
            current = temp
        self.head = sortedHead

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
    array.insertionSort()
    print("-----------------")
    print("Lista ordenada:")
    array.printList()

if __name__ == "__main__":
    main()
