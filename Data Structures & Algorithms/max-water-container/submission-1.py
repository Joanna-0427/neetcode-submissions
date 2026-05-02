class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        contain = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            contain = max(contain,area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1
        return contain

        