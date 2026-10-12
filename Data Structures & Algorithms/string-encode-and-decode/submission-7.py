class Solution:

    def encode(self, strs: List[str]) -> str:
        # we need to encode with a number with the words len then a special
        # character, this way when decoding, we can prune each '4*' then 
        # iterate four accross starting from the delim char 
        # this way whenever we check for the special char 
        final = ""
        delim = "*"
        for s in strs:
            length = len(s)
            final += str(length) + delim + s 
        return final


    def decode(self, s: str) -> List[str]:
        final = []
        i =0 
        while i< len(s):
            j = i
            while s[j] != '*':
                j+=1
            length = int(s[i:j])
            i = j +1
            j = i + length 
            final.append(s[i:j])
            i = j 
        return final
        