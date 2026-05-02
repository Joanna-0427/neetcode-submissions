class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        dic = {'[':']','{':'}','(':')'}
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            elif stack and dic[stack[-1]] == i:
                stack.pop(-1)
            else:
                return False
        return not stack 



            

        