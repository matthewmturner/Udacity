class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LRU_Cache:

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.cache_mapper = dict()
        self.cache_capacity = capacity
        self.cache_size = 0 
        self.cache_tracker_head = None # LinkedList head
        self.cache_tracker_tail = None # LinkedList tail

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.cache_size == 0:
            new_node = Node(value)
            self.cache[key] = new_node
            self.cache_tracker_head = new_node
            self.cache_tracker_tail = new_node
            self.cache_size += 1
        # If cache is at capcity remove LRU and add new value
        elif self.cache_size == self.cache_capacity:
            new_node = Node(value)
            lru_key = self._remove_tail()
            self._add_head(new_node)
            self.cache[key] = new_node
            del self.cache[lru_key]
        # If cache is not at capacity add new value
        else:
            new_node = Node(value)
            self.cache[key] = new_node
            self._add_head(new_node)
            self.cache_size += 1

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        if self.cache.get(key) is None:
            return -1
        else:
            node = self.cache[key]
            # If key exists and is not head then remove current placement, add to head
            # and return value
            if key != self.cache_tracker_head.value:
                self._remove_node(node)
                self._add_head(node)
                return node.value
            # If key exists and is head then return value
            return node.value

    def _add_head(self, node):
        # Add new head by making new node next to old head and 
        # old head previous to new node
        old_node = self.cache_tracker_head
        node.next = old_node
        old_node.previous = node
        self.cache_tracker_head = node
    
    def _remove_tail(self):
        # Remove tail and return key to delete from cache
        lru_key = self.cache_tracker_tail.value
        self.cache_tracker_tail.previous.next = None
        self.cache_tracker_tail = self.cache_tracker_tail.previous

        return lru_key

    def _remove_node(self, node):
        # Remove node after it has been used
        node.previous.next = node.next
        if node.next is not None:
            # If not tail set previous of next to previous
            node.next.previous = node.previous
        else:
            return self._remove_tail()

    def __repr__(self):
        s = "Cache:\n"
        for k,v in self.cache.items():
            s += f"Key({k}): {v.value}\n"
        return s

    def __len__(self):
        return self.cache_size



our_cache = LRU_Cache(5)

our_cache.set(1, 1)
print(f"Current head: {our_cache.cache_tracker_head.value}")
print(f"Current tail: {our_cache.cache_tracker_tail.value}")
our_cache.set(2, 2)
print(f"Current head: {our_cache.cache_tracker_head.value}")
print(f"Current tail: {our_cache.cache_tracker_tail.value}")
our_cache.set(3, 3)
print(f"Current head: {our_cache.cache_tracker_head.value}")
print(f"Current tail: {our_cache.cache_tracker_tail.value}")
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))
print(our_cache)

our_cache.set(7, 7)
our_cache.set(8, 8)
our_cache.get(2)

our_cache.set(10, 10)
print(our_cache)
print(len(our_cache))