class HashTable:
    def __init__(self):
        self.table={}
        
    def _hash(self,key):
        return hash(key) % 10
        
    def insert(self, key, value):
        hashedKey = self._hash(key)
        if hashedKey not in self.table:
            self.table[hashedKey] = []
        self.table[hashedKey].append((key, value))
        
    def search(self, key):
        hashed_key = self._hash(key)
        if hashed_key in self.table:
            for k, v in self.table[hashed_key]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        hashedKey = self._hash(key)
        if hashedKey in self.table:
            self.table[hashedKey] = [(k, v) for k, v in self.table[hashedKey] if k != key]
            if not self.table[hashedKey]:  
                del self.table[hashedKey]

    def __str__(self):
        return str(self.table)
        
        
hashTable = HashTable()
hashTable.insert('key1', 1)
hashTable.insert('key2', 2)
hashTable.insert('key1', 3)  
print(hashTable.search('key1'))  
print(hashTable)
hashTable.delete('key1')
print(hashTable)
