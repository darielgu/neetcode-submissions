class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        greatest = 0
        for num in num_set:
            if (num-1) not in num_set: #denotes start of potential sequence
                current = num
                curr_sequence = 1
                while (current + 1) in num_set:
                    current +=1
                    curr_sequence +=1 
                if (curr_sequence > greatest):
                    greatest = curr_sequence
        return greatest
