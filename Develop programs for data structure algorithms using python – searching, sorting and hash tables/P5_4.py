class HashTable:
    def __init__(self):
        self.size = 10  # Size of the hash table
        self.table = [[] for _ in range(self.size)]  # Initialize an empty hash table

    def _hash_function(self, key):
        # Generate a hash value using the modulo operator
        return hash(key) % self.size

    def insert(self, key, value):
        hash_value = self._hash_function(key)
        self.table[hash_value].append((key, value))

    def search(self, key):
        hash_value = self._hash_function(key)
        for item in self.table[hash_value]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        hash_value = self._hash_function(key)
        for index, item in enumerate(self.table[hash_value]):
            if item[0] == key:
                del self.table[hash_value][index]
                return True
        return False


# Usage:
hash_table = HashTable()

# Inserting key-value pairs
hash_table.insert('apple', 'red')
hash_table.insert('banana', 'yellow')
hash_table.insert('cherry', 'red')

# Searching for a value
print(hash_table.search('apple'))  # Output: red
print(hash_table.search('mango'))  # Output: None

# Deleting a key-value pair
print(hash_table.delete('banana'))  # Output: True

# Searching again after deletion
print(hash_table.search('banana'))  # Output: None
