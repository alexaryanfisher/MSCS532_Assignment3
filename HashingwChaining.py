"""
Assignment 3: Hashing with Chaining, Part 2

Hash Table with Chaining implementation in Python.
This implementation uses a hash table with chaining to handle collisions.
Each bucket in the hash table is a list storing key-value pairs.
"""

# Define a class for the hash table.

class HashTableChaining:
    # Initialize the hash table with a specified capacity. Capacity if the initial number of buckets in the hash table.
    # Default capacity is set to 5.
    def __init__(self, capacity_size=5):
        self.capacity = capacity_size
        #Create a list of empty lists (buckets) for chaining.
        self.table = [[] for _ in range(self.capacity)]
        #Current number of key-value pairs in the hash table.
        self.size = 0

    # Calculate the hash value for a given key.
    def _hash (self, key):
        # Use Python's built-in hash function and modulo operation to ensure the hash value fits within the table's capacity.
        return hash(key) % self.capacity
    
    # Add a key-value pair to the hash table.
    def insert(self, key, value):
        index = self._hash(key)
        chain = self.table[index]
        # Check if the key already exists in the bucket. k = existing key, v = existing value.
        for i, (k, v) in enumerate(chain):
            if k == key:
                # If the key exists, update its value.
                chain[i] = (key, value)
                # Print a message indicating the key was updated.
                print(f"Key '{key}' updated with value '{value}'at index {index}.")
                return
        # If the key does not exist, append the new key-value pair to the bucket.
        chain.append((key, value))
        self.size += 1
        # Print a message indicating the key-value pair was added.
        print(f"Key '{key}' added with value '{value}' at index {index}.")

    # Retrieve the value associated with a given key.
    def search(self, key):
        index = self._hash(key)
        chain = self.table[index]
        # Search for the key in the bucket.
        for k, v in chain:
            if k == key:
                # If found, return the value.
                # Print a message indicating the key was found.
                print(f"Key '{key}' found with value '{v}' at index {index}.")
                return v
        
        # If not found, return None.
        # Print a message indicating the key was not found.
        print(f"Key '{key}' not found in the hash table.")
        return None

    # delete a key-value pair from the hash table.
    def delete(self, key):
        index = self._hash(key)
        chain = self.table[index]
        # Search for the key in the bucket.
        for i, (k, v) in enumerate(chain):
            if k == key:
                # If found, remove the key-value pair from the bucket.
                del chain[i]
                self.size -= 1
                # Print a message indicating the key was removed.
                print(f"Key '{key}' removed from index {index}.")
                return True
        # If the key was not found, return False.
        # Print a message indicating the key was not found.
        print(f"Key '{key}' not found in the hash table.")
        return False
    
    # Display current number of key-value pairs in the hash table.
    def __len__(self):
        return self.size
    
# Display the hash table's contents.
    def __str__(self):
        result = "Hash Table Contents:\n"
        # Returns a string representation of the hash table.
        for i, chain in enumerate(self.table):
            result += f"---- Bucket {i}: {chain}\n"
        result += f"Total key-value pairs: {self.size} -----\n"
        return result
    
# Use Cases for Hash Table with Chaining

if __name__ == "__main__":
    # Create a hash table with chaining.
    hash_table = HashTableChaining(capacity_size=6)

    # Use Case 1: Adding key-value pairs.
    print("Use Case 1: Adding key-value pairs")
    hash_table.insert("dog", 10)
    hash_table.insert("cat", 20)
    hash_table.insert("fish", 30)
    hash_table.insert("rabbit", 40)
    hash_table.insert("lizard", 50)
    hash_table.insert("turtle", 60) # May cause a collision with "dog" or "cat".
    hash_table.insert("ferret", 70) # May cause a collision with "fish" or "rabbit".
    print("\n" + str(hash_table))

    # Use Case 2: Retrieving values.
    print("\nUse Case 2: Retrieving values")
    print("Value for 'cat':", hash_table.search("cat"))
    print("Value for 'dog':", hash_table.search("dog"))
    # Attempt to retrieve a non-existent key.
    print("Value for 'pig':", hash_table.search("pig"))
    print("\n" + str(hash_table))  

    # Use Case 3: Removing key-value pairs.
    print("\nUse Case 3: Removing key-value pairs")
    hash_table.delete("lizard")
    print("\n" + str(hash_table))
        