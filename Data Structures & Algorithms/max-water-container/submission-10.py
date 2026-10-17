class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # amt to trap = r -l * min(heights[l],heights[r])
        water = 0
        l = 0 
        r = len(heights)-1
        while l < r:
            curr = (r-l) * min(heights[l], heights[r])
            water = max(water, curr)
            if heights[l] > heights[r]:
                r -=1
            else:
                l +=1
        return water
