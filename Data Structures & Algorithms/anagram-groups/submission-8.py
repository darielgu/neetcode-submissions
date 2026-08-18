class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            strMap[sortedS].append(s)
        return list(strMap.values())
