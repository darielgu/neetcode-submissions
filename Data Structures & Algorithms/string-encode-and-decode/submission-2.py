class Solution:

    def encode(self, strs: List[str]) -> str:
        delimitter = "@"
        newstr =""
        for string in strs:
            newstr +=  str(len(string)) +delimitter + string
        return newstr

    def decode(self, s: str) -> List[str]:
        master = []
        i = 0
        while i < len(s):
            j = s.find("@", i)
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            master.append(word)
            i = j + 1 + length
        return master