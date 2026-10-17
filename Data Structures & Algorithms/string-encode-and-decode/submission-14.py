class Solution:

    def encode(self, strs: List[str]) -> str:
        # ex ["s" "ariel"] = '1*a5*ariel'
        final = ""
        for s in strs:
            enc = str(len(s)) + '*' + s
            final +=enc
        return final
    def decode(self, s: str) -> List[str]:
        # given "5*Hello5*World" 
        i = 0 
        res = []
        while i < len(s):
            j = i
            while s[j] != '*':
                j +=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            res.append(s[i:j])
            i = j
        return res