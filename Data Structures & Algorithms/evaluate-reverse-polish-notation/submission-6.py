class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                val = a+b
                stack.append(val)
            elif char == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                val = b-a
                stack.append(val)
            elif char == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                val = a*b
                stack.append(val)
            elif char == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                val = b/a
                stack.append(val)
            else:
                stack.append(char)
        return int(stack[0])