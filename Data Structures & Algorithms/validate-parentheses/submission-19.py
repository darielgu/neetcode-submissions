class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracks = { ')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in bracks:
                if stack and stack[-1] == bracks[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False