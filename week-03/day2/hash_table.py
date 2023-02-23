class HashTable:
    def __init__(self) :
        self.table = [[] for i in range(64)]

    def _hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % len(self.table)

    def set(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        self.table[index]
        for data in self.table[index]:
            if data[0] == key:
                return data[1]
            
myHash = HashTable()

myHash.set('name', 'alice')
myHash.set('age', 34)
# myHash.set('mane', 'luxurious')

print(myHash.table)
print(myHash.get('name'))
# print(myHash.get('age'))
# print(myHash.get('mane'))