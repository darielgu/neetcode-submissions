class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        greatest = 0
        for num in myset:
            if (num-1) not in myset:
                current = num
                curr_seq = 1
                while (current+1) in myset:
                    current +=1
                    curr_seq+=1 
                if curr_seq > greatest:
                    greatest = curr_seq
        return greatest

