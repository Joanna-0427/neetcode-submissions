class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        operator = 0
        stack = []
        res = ''
        i = 0

        for i in range(n):
            if s[i].isdigit():
                operator = operator * 10 + int(s[i])
            
            elif s[i] == '[':
                stack.append(operator)
                operator = 0
            
            elif s[i] == ']':
                inner = ''
                while stack and isinstance(stack[-1],str):
                    inner = stack.pop() + inner
                repeat = stack.pop()
                stack.append(inner * repeat)
            
            else:
                stack.append(s[i])
        
        return ''.join(stack)

