class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:return -1
        q = deque(['0000'])
        visited = set(['0000'])
        visited.update(deadends)
        #add(X) X要元组、string、int可哈希；set(X)只要X是可迭代变量就可以，会遍历X里面的元逐个添加 = visited.update(X)

        def children(lock):
            res = []
            for i in range(len(lock)):
                turn1 = lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:]
                turn2 = lock[:i] + str((int(lock[i]) - 1 + 10) % 10) + lock[i+1:]
                res.append(turn1)
                res.append(turn2)
            return res

        level = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return level
                
                for child in children(cur):
                    if child not in visited:
                        q.append(child)
                        visited.add(child)
            
            level += 1

        return -1