class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        l = 0
        r = len(height) -1

        maxLeft = 0
        maxRight = 0
        
        water = 0
        while l <= r:
            if maxRight > maxLeft:
                curr = max(0, maxLeft-height[l])
                maxLeft = max(maxLeft, height[l])
                l+=1
            else:
                curr = max(0, maxRight-height[r])
                maxRight = max(maxRight, height[r])
                r-=1
            water += curr
        return water