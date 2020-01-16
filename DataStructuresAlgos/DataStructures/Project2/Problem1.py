class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def remove_head(self):
        self.head = self.head.next


class LRU_Cache:

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.cache_capacity = capacity
        self.cache_size = 0 
        self.cache_tracker_head = None # LinkedList head
        self.cache_tracker_tail = None # LinkedList tail

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.cache_size == 0:
            self.cache[key] = value
            new_node = Node(value)
            self.cache_tracker_head = new_node
            self.cache_tracker_tail = new_node
            self.cache_size += 1
        elif self.cache_size == self.cache_capacity:
            print(f"Cache at capacity while setting {key}")
            lru_key = self._remove_tail()
            self._add_head(key)
            self.cache[key] = value
            del self.cache[lru_key]
        else:
            self.cache[key] = value
            self._add_head(key)
            self.cache_size += 1

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.cache.get(key) is None:
            return -1
        else:
            if key != self.cache_tracker_head.value:
                self._add_head(key)
                return self.cache[key]
            return self.cache[key]



    # TODO Add functionality to update previous of tail or the equivalent 
    def _add_head(self, value):
        print(f"Adding new head: {value}")
        new_head = Node(value)
        print(f"Old head: {self.cache_tracker_head.value}")
        old_node = self.cache_tracker_head
        new_head.next = old_node
        old_node.previous = new_head
        if self.cache_tracker_head == self.cache_tracker_tail:
            self.cache_tracker_tail.previous = new_head
        print(f"Old node previous after setting to new head: {old_node.previous}")
        self.cache_tracker_head = new_head
    
    def _remove_tail(self):
        print(f"Removing {self.cache_tracker_tail.value} from cache")
        lru_key = self.cache_tracker_tail.value
        print(f"New tail: {self.cache_tracker_tail.previous}")
        self.cache_tracker_tail = self.cache_tracker_tail.previous

        return lru_key

    # def __repr__(self):




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
print(our_cache.cache)

our_cache.set(7, 7)
our_cache.set(8, 8)

print(our_cache.cache)