class HashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table = [[] for _ in range(size)] # Create an empty list of lists
    
    def hash_function(self, key):
        return hash(key) % self.size # Generate index using built-in hash()
        
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key: # Update value if key exists
                pair[1] = value
                return
        self.table[index].append([key, value]) # Append key-value pair
        
    def get(self,key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None # Key not found
    
    def remove(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
    
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# Example test case
ht = HashTable()
ht.insert("name", "Anees")
ht.insert("age", 20)
ht.insert("city", "Malappuram")
ht.display()

print(ht.get("name"))  # Output: Anees
ht.remove("age")
ht.display()


