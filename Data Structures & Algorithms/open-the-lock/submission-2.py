class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        dead = set(deadends)
        def children(lock):
            res = []
            for i in range(4):
                turn1 = str((int(lock[i])+1)% 10) 
                turn2 = str((int(lock[i])-1+10)%10)
                res.append(lock[:i] + turn1 + lock[i+1:])
                res.append(lock[:i] + turn2 + lock[i+1:])
            return res
        
        q = deque(['0000'])
        visited = set('0000')
        level = 0
        while q:
            n = len(q)
            for _ in range(n):
                lock = q.popleft()
                if lock == target:
                    return level
                for child in children(lock):
                    if child not in dead and child not in visited:
                        q.append(child)
                        visited.add(child)
            level += 1
        
        return -1
                

            