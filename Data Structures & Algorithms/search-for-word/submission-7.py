class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
            rows, cols = len(board), len(board[0])
            visited = set()

            def dfs(r,c,i):
                if i == len(word):
                    return True
                
                if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited:
                    return False
                
                if board[r][c] != word[i]:
                    return False
                
                visited.add((r,c))
                for dr, dc in ((0,1),(0,-1),(-1,0),(1,0)):
                    nr, nc = r+dr, c+dc
                    if dfs(nr,nc,i+1):return True
                
                visited.remove((r,c))
                return False
            
            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == word[0]:
                        # return dfs(i,j,0)这个只是试第一个，返回结果
                        if dfs(i,j,0):return True #其他也尝试
            
            return False
