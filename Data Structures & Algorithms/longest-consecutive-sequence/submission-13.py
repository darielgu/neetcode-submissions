class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        longest = 0 
        for num in nums:
            curr = 1
            if (num - 1) not in vals:
                while num + curr in vals:
                    curr+=1
            longest = max(longest, curr)
        return longest 