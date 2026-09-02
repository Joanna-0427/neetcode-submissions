class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(row,col,i):
            if i == len(word):
                return True
                
            if (row < 0 or col < 0 or row >= rows or col >= cols or (row,col) in visited or board[row][col] != word[i]):
                return False
            
            
            visited.add((row,col))

            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_row, new_col = row + dr, col + dc
                if dfs(new_row,new_col,i+1):
                    return True
            
            visited.remove((row,col))
            return False
            
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False

