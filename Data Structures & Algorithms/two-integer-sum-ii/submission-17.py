class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        nums = numbers
        r = len(nums) -1
        while l < r:
            val = nums[l] + nums[r]
            if val == target:
                return [l+1,r+1]
            elif val > target:
                r -=1
            else:
                l+=1
