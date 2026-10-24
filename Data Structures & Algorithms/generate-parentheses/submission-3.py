class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        Open, Close = n, n
        res = []
        path = []

        def dfs(Open, Close):
            if Close < Open:
                return False
            
            if len(path) == 2*n:
                res.append(''.join(path))
                return
            if Open > 0:
                path.append('(')
                dfs(Open-1,Close)
                path.pop()
            if Open < Close:
                path.append(')')
                dfs(Open,Close-1)
                path.pop()
        
        dfs(n,n)
        return res

