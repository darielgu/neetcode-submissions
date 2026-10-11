class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_a = {}
        map_b = {}
        for char in s:
            if char in map_a:
                map_a[char] +=1
            else:
                map_a[char] = 1
        for char in t:
            if char in map_b:
                map_b[char] +=1
            else:
                map_b[char] = 1
        return map_a == map_b