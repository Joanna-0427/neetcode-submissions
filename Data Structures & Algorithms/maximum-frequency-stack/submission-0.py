class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.maxcnt = 0
        self.stack = defaultdict(list)

    def push(self, val: int) -> None:
        valcnt = self.cnt.get(val,0) + 1
        self.cnt[val] = valcnt
        if valcnt > self.maxcnt:
            self.maxcnt = valcnt
        self.stack[valcnt].append(val)
        

    def pop(self) -> int:
        res = self.stack[self.maxcnt].pop()
        if not self.stack[self.maxcnt]:
            self.maxcnt -= 1
        self.cnt[res] -= 1
        return res
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()