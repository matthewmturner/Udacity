class LRU_Cache:

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.capacity = capacity
        self.used = list()
        self.mru = None
        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.cache.get(key) is None:
            return -1
        else:
            if key != self.mru:
                self.used.append(key)
                self.mru = key
            return self.cache[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) == self.capacity:
            print("Cache at capacity")
            self.cache[key] = value
            remove_key = self.used.pop(0)
            del self.cache[remove_key]
            self.used.append(key)
            self.mru = key
        else:
            self.cache[key] = value
            self.used.append(key)
            self.mru = key


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.used)
print(our_cache.get(3))
print(our_cache.cache)
print(our_cache.used)

our_cache.set(7, 7)
our_cache.set(8, 8)

print(our_cache.cache)
print(our_cache.used)