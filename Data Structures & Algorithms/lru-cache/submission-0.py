class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    # remove node from list
    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


    # insert node right after head
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # move to front
        self.remove(node)
        self.insert(node)

        return node.val


    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.remove(node)
            self.insert(node)

        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

            if len(self.cache) > self.cap:
                # remove LRU
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
