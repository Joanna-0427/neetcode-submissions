class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(idx,total):
            if total == target:
                res.append(path[:])
                return
            
            if idx >= len(candidates) or total > target:
                return
            
            
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if total > target:
                    break
                path.append(candidates[i])
                dfs(i+1,total+candidates[i])
                path.pop()
        
        dfs(0,0)
        return res

