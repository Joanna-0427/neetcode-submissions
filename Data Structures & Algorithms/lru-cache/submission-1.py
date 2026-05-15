class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next = nxt
        nxt.prev = pre

    def insert(self,node):
        temp = self.right.prev
        node.next = self.right
        self.right.prev = node
        temp.next = node
        node.prev = temp
       

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
   

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newnode = Node(key,value)
        self.insert(newnode)
        self.cache[key] = newnode

        if len(self.cache) > self.cap:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]
        
        


       
        







        
