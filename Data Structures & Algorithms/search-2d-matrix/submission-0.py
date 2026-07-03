class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m-1
        while l <= r:
            mid = (l + r)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                l = mid + 1
        
        nl, nr = 0, n-1
        while nl <= nr:
            mid = (nl + nr)//2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] > target:
                nr = mid - 1
            elif matrix[r][mid] < target:
                nl = mid + 1
        return False

