class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
    def __repr__(self):
        return "{3} (k: {0} v: {1})".format(self.key, self.val)
    def __str__(self):
        return self.__repr__()

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key].val
        self._update(key, val)

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._update(key, value)
            return

        if len(self.cache) == self.capacity:
            self._evict()

        self._insert(key, value)

    def _remove(self, key):
        node = self.cache[key]
        prev = node.prev
        next = node.next
        if prev:
            if self.tail == node:
                self.tail = prev
            prev.next = next
        if next:
            if self.head == node:
                self.head = next
            next.prev = prev
        self.cache.pop(key)

    def _update(self, key, val):
        self._remove(key)
        self._insert(key, val)

    def _insert(self, key, val):
        new_head = Node(key, val)
        if self.head is None:
            self.head = new_head
            self.tail = new_head
        else:
            old_head = self.head
            old_head.prev = new_head
            new_head.next = old_head
            self.head = new_head
        self.cache[key] = new_head

    def _evict(self):
        old_tail = self.tail
        self.cache.pop(old_tail.key)

        self.tail = old_tail.prev
        self.tail.next = None

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)