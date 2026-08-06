class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue # if i and i+1 are the same skip,
            # else start while loop from 
            j = i +1
            k = len(nums) -1
            target = -nums[i]

            while j < k:
                if (nums[k] + nums[j]) == target:
                    final.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                elif (nums[j] +nums[k] < target):
                    j +=1
                else:
                    k -=1
        return final