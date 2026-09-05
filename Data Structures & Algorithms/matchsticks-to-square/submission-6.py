class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False
        target = total // 4
        used = [False] * len(matchsticks)
        matchsticks.sort(reverse=True)

        def dfs(i,k,subsetsum):
            if k == 0:
                return True
            
            if subsetsum == target:
                return dfs(0,k-1,0)
            
            for j in range(i,len(matchsticks)):
                if used[j] or subsetsum + matchsticks[j] > target:
                    continue
                
                used[j] = True
                #前j个可能已经用过，或者可能太大跳过了，不需要回头看，使用j+1
                if dfs(j+1,k,subsetsum+matchsticks[j]):
                    return True
                used[j] = False
            
            return False
        
        return dfs(0,4,0)
