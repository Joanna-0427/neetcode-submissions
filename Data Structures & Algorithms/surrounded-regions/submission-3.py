class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board),len(board[0])
        
        def dfs(i,j):
            if i < 0 or (i > rows-1) or j < 0 or (j > cols-1) or board[i][j] != 'O':
                return
            #和边界相连的也都安全
            board[i][j] = 'T'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for r in range(rows):
            for c in range(cols):
                if r in [0,rows-1] and board[r][c] == 'O':
                    dfs(r,c)
                
                if c in [0,cols-1] and board[r][c] == 'O':
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
        
        


