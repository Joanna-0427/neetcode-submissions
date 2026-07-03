class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                area = (i - index) * height
                maxarea = max(maxarea,area)
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxarea = max(maxarea, h * (len(heights) - i))
        return maxarea