class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board),len(board[0])
        
        def dfs(i,j):
            #是T、X都不用标记，和边界O相连的O标记，这些相连的O后续都不改变
            if i < 0 or (i > rows-1) or j < 0 or (j > cols-1) or board[i][j] != 'O':
                return
            
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
        
        
        


