class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through the array with a complement and seen 
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i
        return []
                