class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #mapper边界或者是'abc'，或者['a','b','c']；不能2:'a','b','c'
        mapper = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'}

        res = []
        path = []
        if not digits:
            return res
        
        def dfs(i):
            if i == len(digits):
                res.append(''.join(path))
                return
            
            for j in range(len(mapper[digits[i]])):
                ch = mapper[digits[i]][j]
                path.append(ch)
                dfs(i+1)
                path.pop()

        dfs(0)
        return res



