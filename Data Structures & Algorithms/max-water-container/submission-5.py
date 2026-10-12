class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width r - l 
        # height min(heights[r],heights[l])
        l = 0 
        r = len(heights) -1
        area = (r - l) * min(heights[r],heights[l])
        while l < r:
            area = max(area,(r - l) * min(heights[r],heights[l]))
            if heights[l] > heights[r]:
                r -=1
            else:
                l+=1
        return area 