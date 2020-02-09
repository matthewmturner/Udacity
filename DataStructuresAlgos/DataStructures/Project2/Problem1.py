class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LRU_Cache:
    def __init__(self, capacity):
        """Initialize LRU (least recently used) cache object.
        
        Arguments:
            capacity {int} -- The max number of objects to hold in cache. 
        """
        self.cache = dict()
        self.cache_capacity = capacity
        self.cache_size = 0
        self.cache_tracker_head = None  # LinkedList head
        self.cache_tracker_tail = None  # LinkedList tail

    def set(self, key, value):
        """Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        
        Arguments:
            key {hashable type} -- key used to identify item in cache
            value {any object} -- value to be held in cache associate to key
        """
        if self.cache_capacity <= 0:
            pass
        elif self.cache.get(key) is not None:
            new_node = Node(value)
            self.cache[key] = new_node
            self._add_head(new_node)
        elif self.cache_size == 0:
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
        """ Retrieve item from provided key. Return -1 if nonexistent.
        
        Arguments:
            key {hashable type} -- key to identify item in cache
        
        Returns:
            [any object] -- value associated to key
        """

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
        for k, v in self.cache.items():
            s += f"Key({k}): {v.value}\n"
        return s

    def __len__(self):
        return self.cache_size


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)

print(our_cache.get(1))
# Expected output: 1
print(our_cache.get(9))
# Expected output: -1 because 9 is not present in the cache
our_cache.set(6, 6)
print(our_cache)
# Expected output:
# {1,1,
# 3:3,
# 4:4,
# 5:5,
# 6:6}
our_cache.set(3, 10)
print(our_cache)
# Expected output:
# {1,1,
# 3:10,
# 4:4,
# 5:5,
# 6:6}
neg_cache = LRU_Cache(-5)
print(neg_cache.set(1,1))
# Expected output: None
print(neg_cache.get(1))
# Expected output: None
