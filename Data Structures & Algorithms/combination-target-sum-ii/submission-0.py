class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        total = 0

        def dfs(start):
            nonlocal total
            #total==target放在判断最前面，如果i是最后一个元素i+1直接return结果则添加不进去
            if total == target:
                res.append(path[:])
                return
            #其次再是i的判断
            if start >= len(candidates) or total > target:
                return
            
            #每次start开始，都检查剩下的元素在同一层递归里，有没有重复的，如果有重复的continue
            #检查的是在同一层的重复，如果不同层，重复不会受影响
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                #total,path是全局变量，所以需要回退，如果是每层的新参数，则可以不用
                path.append(candidates[i])
                total += candidates[i]
                #i+1下一层,不受上一层影响，即i+1 == i,不影响
                dfs(i+1)
                path.pop()
                total -= candidates[i]
        
        dfs(0)
        return res
            


