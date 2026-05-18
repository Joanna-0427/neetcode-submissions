class MyHashSet:

    def __init__(self):
        self.d = {}
        

    def add(self, key: int) -> None:
        self.d[key] = None
    

    def remove(self, key: int) -> None:
        if key not in self.d:
            return
        del self.d[key]
        

    def contains(self, key: int) -> bool:
        if key not in self.d:
            return False
        return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)