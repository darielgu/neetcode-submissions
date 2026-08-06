class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # declare array for result 
        # forward pass update then multiply
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # backward pass update than multiply
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res