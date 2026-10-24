class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        if not digits:return []

        res = []
        path = []
        def dfs(idx):
            if idx == len(digits):
                res.append(''.join(path[:]))
                return
            

            for digit in mapping[digits[idx]]:
                path.append(digit)
                dfs(idx+1)
                path.pop()
        
        dfs(0)
        return res