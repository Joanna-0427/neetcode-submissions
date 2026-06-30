class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1+v2)
            elif t == '-':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2-v1)
            elif t == '*':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2*v1)
            elif t == '/':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2/v1))
            else:
                stack.append(int(t))
        return stack[-1]