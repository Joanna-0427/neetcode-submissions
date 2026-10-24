class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0: return False
        target = total // 4
        matchsticks.sort(reverse=True)

        edges = [0] * 4
        def dfs(idx,target):
            if idx >= len(matchsticks): #每条边都小于target，但所有火柴都放进去了，总和4*target，所以每边一定=target

                return True
            

            for i in range(4):
                if edges[i] + matchsticks[idx] <= target:
                    edges[i] += matchsticks[idx]
                    if dfs(idx+1,target):return True
                    edges[i] -= matchsticks[idx]
            
            return False

        return dfs(0,target)
            

            


