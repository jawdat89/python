class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        
        self.left, self.right = Node(0, 0), Node(0, 0) # LRU - left, MRU - right
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt =  node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node): 
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # update node to be the most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # return the value
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            # node is already exist, remove first
            self.remove(self.cache[key])
        # create the new node
        self.cache[key] = Node(key, value)
        # insert into the linked list
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # capacity exceeded, remove from the list and delete the LRU from the cache(hasmap)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
