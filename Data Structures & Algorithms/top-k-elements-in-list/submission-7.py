class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # create a dictionary with values and how many times they appear
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1
        arr = []
        for num, count in freq.items():
            arr.append([count, num])

        arr.sort()
        res = []
        i = 0
        while i < k:
            res.append(arr.pop()[1])
            i +=1
        return res
