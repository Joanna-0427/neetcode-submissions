class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        operator = {'+','-','*','/'}
        for i in range(n):
            if tokens[i] not in operator:
                stack.append(int(tokens[i]))
            else:
                first = stack.pop()
                second = stack.pop()
                if tokens[i] == '+':
                    total = first + second
                    stack.append(total)
                elif tokens[i] == '-':
                    total = second - first
                    stack.append(total)
                elif tokens[i] == '/':
                    total = int(second / first)
                    stack.append(total)
                elif tokens[i] == '*':
                    total = first * second
                    stack.append(total)
        return stack[0]



        