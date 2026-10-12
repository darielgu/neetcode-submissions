class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        # at every index the amount of water you can trap is max of whatever side ur closest to - current height
        l = 0 
        r = len(height) -1 
        maxLeft = height[l]
        maxRight = height[r]

        
        while l < r:
            # update condition 
            if maxRight < maxLeft:
                trapped += max(0, (maxRight - height[r]))
                r -=1
                if maxRight < height[r]:
                    maxRight = height[r]
            else:
                trapped += max(0, (maxLeft - height[l]))
                l+=1
                if maxLeft < height[l]:
                    maxLeft = height[l]




        return trapped 