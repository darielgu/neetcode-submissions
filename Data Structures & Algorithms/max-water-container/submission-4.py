class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #The height is limited by the shorter line, so to potentially increase the area, we must move the pointer at the shorter line inward.
        #Moving the taller line never helps because it keeps the height the same but reduces the width
        left = 0 
        right = len(heights) -1
        res = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            if res < area:
                res = area
            if heights[left] <= heights[right]:
                left +=1
            else:
                right -=1
        return res
