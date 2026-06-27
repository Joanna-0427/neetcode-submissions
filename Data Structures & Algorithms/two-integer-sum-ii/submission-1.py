class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left, right = 0, len(numbers)-1
        # while left < right:
        #     val = numbers[left] + numbers[right]
        #     if val < target:
        #         left += 1
        #     elif val > target:
        #         right -= 1
        #     else:
        #         return [left+1, right+1]

        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            val = target - numbers[i]
            while l <= r:
                mid = (l+r) // 2
                if numbers[mid] < val:
                    l += 1
                elif numbers[mid] > val:
                    r -= 1
                else:
                    return [i+1,mid+1]
        return []



