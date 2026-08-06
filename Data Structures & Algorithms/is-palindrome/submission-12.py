class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        s = ''.join(filter(str.isalnum, s)).lower() # so we remove 

        print(s)
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left +=1 
            right -=1
        return True