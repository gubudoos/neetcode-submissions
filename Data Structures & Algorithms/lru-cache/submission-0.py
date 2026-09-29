class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # cache stores: [key] = Node(key, val)
        self.cache = {}

        # init left and right node that point to each other
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left
        self.left.prev = self.right.nxt = None

    def insert(self, node):
        # insert node just before 'right' node
        # Node(3) - right -> becomes -> Node(3) - Node(4) - right
        nxt = self.right
        prev = self.right.prev

        prev.nxt = node
        nxt.prev = node
        node.nxt = nxt
        node.prev = prev

    def remove(self, node):
        # remove node and fix pointers for prev and next node
        nxt = node.nxt
        prev = node.prev
        prev.nxt = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            res = self.cache[key].val
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            NodeToBeRemoved = self.left.nxt
            self.remove(NodeToBeRemoved)
            del self.cache[NodeToBeRemoved.key]
        
