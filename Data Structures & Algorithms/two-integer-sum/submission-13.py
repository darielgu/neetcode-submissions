class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_map = {}
        for i in range(len(nums)):
            n_map[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] in n_map and n_map[target-nums[i]] != i:
                return [i, n_map[target-nums[i]]]
                