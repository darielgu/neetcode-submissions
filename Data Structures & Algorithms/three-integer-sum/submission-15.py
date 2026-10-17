class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            #start pointer 2 sum
            l = i+1
            r = len(nums)-1
            while l<r:
                tsum = nums[i] + nums[l] + nums[r]
                if tsum >0:
                    r -=1
                elif tsum <0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l +=1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1
            i +=1
        return res
