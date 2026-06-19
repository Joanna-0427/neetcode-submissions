class Solution:
    def isValid(self, s: str) -> bool:
        # if not s:
        #     return True

        # dic = {'[':']','{':'}','(':')'}
        # stack = []
        # for i in s:
        #     if i in dic:
        #         stack.append(i)
        #     elif stack and dic[stack[-1]] == i:
        #         stack.pop(-1)
        #     else:
        #         return False
        # return not stack 


        if not s:
            return True
        
        dic = {'[':']','{':'}','(':')'}
        stack = []
        for ch in s:
            if ch in dic:
                stack.append(ch)
            elif stack and dic[stack[-1]] == ch:
                stack.pop()
            else:
                return False
        return not stack



            

        