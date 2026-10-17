class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums1 = set(nums)
        largest = 0 
        for num in nums:
            longest = 0
            if num-1 not in nums1:
                i = num
                while i in nums1:
                    longest +=1
                    i +=1
            largest = max(largest,longest)

        return largest