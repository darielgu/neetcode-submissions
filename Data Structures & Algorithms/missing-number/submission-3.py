class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mySet = set(range(len(nums)+1))
        for num in nums:
            mySet.discard(num)
        if mySet:
            return mySet.pop()
        