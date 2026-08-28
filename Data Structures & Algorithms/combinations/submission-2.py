class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(start,count):
            if count == k:
                res.append(path[:])
                return
            
            if start > n:
                return
            #for循环版本，站在每一层看剩下的每层还有多少元素可以决策，每层元素不固定；
            #每层分支剩余数都在减少，通常更高效
            
            for i in range(start,n+1):
                path.append(i)
                dfs(i+1,count+1)
                path.pop()
        
        dfs(1,0)
        return res
        