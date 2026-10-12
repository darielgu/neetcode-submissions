class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width r - l 
        # height min(heights[r],heights[l])
        l = 0
        r = len(heights) -1
        area  = 0 
        while l <r:
            w = r-l
            h = min(heights[r],heights[l])
            area = max(area, w*h)
            if heights[l] > heights[r]:
                r -=1
            else:
                l+=1
        return area