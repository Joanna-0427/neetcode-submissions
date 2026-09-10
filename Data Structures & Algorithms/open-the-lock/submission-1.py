class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #求最短的路径，用BFS
        if '0000' in deadends:
            return -1
        
        
        def children(lock):
            #每次调用children都是一个全新的、空的res；多次调用互不影响；
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                #不能直接写lock变量会覆盖lock后面的digit是在错误的lock上修改的
                # lock = lock[:i] + digit + lock[i+1:]
                res.append(lock[:i] + digit + lock[i+1:])

                digit = str((int(lock[i]) - 1 + 10) % 10)
                # lock = lock[:i] + digit + lock[i+1:]
                res.append(lock[:i] + digit + lock[i+1:])
            
            return res
        
        #deadends不能在继续访问，放在visited里面，相当于de = set(deadends),if child not in de:
        visited = set(deadends)
        q = deque([('0000',0)])

        while q:
            for _ in range(len(q)):
                lock, turn = q.popleft()
                if lock == target:
                    return turn
                for child in children(lock):
                    if child not in visited:
                        q.append((child,turn+1))
                        visited.add(child)
        return -1

            