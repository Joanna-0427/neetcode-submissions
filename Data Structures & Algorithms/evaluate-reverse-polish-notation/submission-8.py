class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        operator = {'+','-','*','/'}
        for i in range(n):
            if tokens[i] not in operator:
                stack.append(int(tokens[i]))
            elif tokens[i] == '+':
                first = stack.pop()
                second = stack.pop()
                total = first + second
                stack.append(total)
            elif tokens[i] == '-':
                first = stack.pop()
                second = stack.pop()
                total = second - first
                stack.append(total)
            elif tokens[i] == '/':
                first = stack.pop()
                second = stack.pop()
                total = int(second / first)
                stack.append(total)
            elif tokens[i] == '*':
                first = stack.pop()
                second = stack.pop()
                total = first * second
                stack.append(total)
        return stack[0]



        