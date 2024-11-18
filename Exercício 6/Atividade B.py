class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableLinkedList:
    def __init__(self):
        self.table = [None] * 10  

    def _hash(self, key):
        return hash(key) % 10

    def insert(self, key, value):
        hashedKey = self._hash(key)
        newNode = Node(key, value)
        
        if self.table[hashedKey] is None:
            self.table[hashedKey] = newNode
        else:
            current = self.table[hashedKey]
            while current:
                if current.key == key:
                    current.value = value  
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = newNode

    def search(self, key):
        hashedKey = self._hash(key)
        current = self.table[hashedKey]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        hashedKey = self._hash(key)
        current = self.table[hashedKey]
        prev = None
        
        while current:
            if current.key == key:
                if prev is None:  
                    self.table[hashedKey] = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

    def __str__(self):
        return str([(i, self._getValues(i)) for i in range(len(self.table))])

    def _getValues(self, index):
        values = []
        current = self.table[index]
        while current:
            values.append((current.key, current.value))
            current = current.next
        return values

def main():
    hashTableLl = HashTableLinkedList()
    hashTableLl.insert('key1', 'value1')
    hashTableLl.insert('key2', 'value2')
    hashTableLl.insert('key1', 'value3')  
    print("---------------------------------")
    print("Busca por 'key1':",hashTableLl.search('key1'))  
    print("Tabela hash:",hashTableLl)
    print("---------------------------------")
    hashTableLl.delete('key1')
    print("Tabela hash após deletar 'key1':",hashTableLl)

if __name__ == "__main__":
    main()
