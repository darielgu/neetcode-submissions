class Solution:
    def isValid(self, s: str) -> bool:
        val = {
        ')': '(',
        '}': '{',
        ']': '['
        }
        stack = []
        for char in s:
            if char in val.values():
                stack.append(char)
            if char in val.keys():
                if stack and stack[-1] == val[char]:
                    stack.pop()
                else:
                    return False
            

        if not stack:
            return True
        return False
        