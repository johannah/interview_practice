

# hash table is O(1) time complexity
# hash table is O(n) memory

hash_tables = [None for i in 1000]
hash_tables[hash(thing) % 1000] = thing


