class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        self.s.append(val)
        
        r = min(val,self.m[-1] if self.m else val)
        self.m.append(r)

    def pop(self) -> None:
        if not self.s:
            return None
        self.s.pop()
        self.m.pop()

    def top(self) -> int:
        if self.s:
            return self.s[-1]

    def getMin(self) -> int:
        if self.m:
            return self.m[-1]
        
