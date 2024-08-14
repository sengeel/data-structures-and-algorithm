# class HashTable:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [None for i in range (self.MAX)]

#     def get_hash(self, key):
#         h = 0
#         for char in key:
#          h += ord(char)
#         return h % self.MAX
    
#     def __setitem__(self, key, val):
#        h = self.get_hash(key)
#        self.arr[h] = val

#     def __getitem__(self, key):
#        h = self.get_hash(key)
#        return self.arr[h]
    
#     def __delitem__(self, key):
#        h = self.get_hash(key)
#        self.arr[h] = None
       
        

# t = HashTable()
# t['march 6'] = 130
# t['march 1'] = 20
# t['dec 17'] = 130
# print(t['dec 17'])
# print(t.arr)


#  PREVENTING COLLISION

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def find(self, key):
        a = self.head

        while a is not None:
            if a.key == key:
                return a.value
            a= a.next
        return None
    
    def delete(self, key):
        a = self.head
        prev = None

        while a is not None:
            if a.key == key:
                if prev is not None:
                    prev.next = a.next
                else:
                    self.head = a.next
                return True
            
            prev = a 
            a = a.next
        return False


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size  # Compute the drawer number using the key
    
    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].insert(key, value)
    
    def search(self, key):
        index = self._hash(key)
        return self.table[index].find(key)
    
    def delete(self, key):
        index = self._hash(key)
        self.table[index].delete(key)




         

hash_table = HashTable()

# Insert key-value pairs
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)

# Find values by key
print(hash_table.search("apple"))   # Output: 1
print(hash_table.search("banana"))  # Output: 2

# Delete a key
hash_table.delete("banana")

# Try to find a deleted key
print(hash_table.search("banana"))  # Output: None




          

       




    