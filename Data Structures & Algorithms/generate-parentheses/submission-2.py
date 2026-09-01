class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        

        def dfs(OpenCount,CloseCount):
            if len(path) == 2 * n:
                res.append(''.join(path))
                return
            
            if OpenCount < n:  
                path.append('(')
                dfs(OpenCount+1,CloseCount)
                path.pop()
            if CloseCount < OpenCount:
                path.append(')')
                dfs(OpenCount,CloseCount+1)
                path.pop()
            
        
        dfs(0,0)
        return res



        