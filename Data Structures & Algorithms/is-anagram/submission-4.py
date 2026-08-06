class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars1 = {}
        chars2 = {}
        for char in s:
            chars1[char] = 1 + chars1.get(char,0)
        for char in t:
             chars2[char] = 1 + chars2.get(char,0)
        if chars1 == chars2:
            return True
        return False