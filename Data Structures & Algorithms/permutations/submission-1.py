class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def dfs(path):
            if len(path) >= len(nums):
                res.append(path.copy())
                return
            
            for n in nums:
                if n in used:
                    continue
                path.append(n)
                used.add(n)
                dfs(path)
                path.pop()
                used.remove(n)

        dfs([])
        return res
        

            