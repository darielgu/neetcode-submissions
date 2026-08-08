class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of nums | quick lookup for start of sequence
        numset = set(nums)

        longest = 0 # track longest 

        # iterate through nums, if num-1 does not exist this is a potential     
        # sequence start. When a sequence is found while iteration to see if 
        # next num in sequence exists
        
        for num in numset:
            if (num - 1) not in numset:
                length = 1
                while (num+length in numset):
                    length +=1
                longest = max(length, longest)
        return longest