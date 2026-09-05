class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        target = sum(matchsticks) // 4
        edges = [0] * 4
        #提前失败，返回False
        matchsticks.sort(reverse=True)
        
        def dfs(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if edges[j] + matchsticks[i] <= target:
                    edges[j] += matchsticks[i]
                    if dfs(i+1):
                        return True

                    edges[j] -= matchsticks[i]
                
            return False
        
        return dfs(0)






            


