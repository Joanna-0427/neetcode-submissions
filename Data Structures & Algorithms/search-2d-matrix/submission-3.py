class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l,r = 0, row-1
        while l<= r:
            mid = (l+r) // 2
            if matrix[mid][0] == target:
                return True
            
            if matrix[mid][0] < target:
                l = mid + 1
            
            if matrix[mid][0] > target:
                r = mid - 1
        
        left, right = 0, col-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[r][mid] == target:
                return True
            
            if matrix[r][mid] < target:
                left = mid + 1
            
            if matrix[r][mid] > target:
                right = mid - 1
        
        return False