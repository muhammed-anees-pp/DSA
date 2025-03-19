# Create a hash table using a dictionay
hash_table = {}

# Insert values (0(1)) average time
hash_table["name"] = "Anees"
hash_table["age"] = 20
hash_table["city"] = "Malappuram"


# Access values (O(1) average time)
print(hash_table["name"])  # Output: Anees

# Delete a key (O(1) average time)
del hash_table["age"]

# Check if key exists
print("age" in hash_table)  # Output: False
