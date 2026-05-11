class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = height[0]
        maxright = height[-1]
        total = 0
        left = 0
        right = len(height) - 1

        while left < right:
            if maxleft < maxright:
                left += 1
                maxleft = max(height[left],maxleft)
                total += maxleft - height[left]
            else:
                right -= 1
                maxright = max(height[right],maxright)
                total += maxright - height[right]
        
        return total


             


        