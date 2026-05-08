class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(openN,closedN):
            if openN == closedN == n:
                res.append(''.join(path))
                return
            
            if openN < n:
                path.append('(')
                dfs(openN+1,closedN)
                path.pop()
            
            if closedN < openN:
                path.append(')')
                dfs(openN,closedN+1)
                path.pop()

        dfs(0,0)
        return res