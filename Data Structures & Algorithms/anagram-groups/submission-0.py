class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # basically want to create a hasmap with letters in 
        res = defaultdict(list) # default dict makes it that no key error will exitst, non mapped character have val of 0 
        for s in strs:
            count = [0] * 26 # list of 0s for each char in 
            for c in s: # for each character in the string from the list 
            # here we add 1 to the ascii value corresponding to that character
                count[ord(c) - ord('a')] += 1 # ord gives us the ascii value 
            res[tuple(count)].append(s) # key is that list of a - z and our value is the str 
        return res.values()