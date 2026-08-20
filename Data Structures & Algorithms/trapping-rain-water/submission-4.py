class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        if len(height) <= 1:
            return 0

        l = 0
        r = len(height)-1
        l_h = height[l]
        r_h = height[r]

        l_w = 0
        r_w = 0

        while l < r:
            if height[l] > height[r]:
                r-=1
                if r_h > height[r]:
                    r_w += r_h-height[r]
                else:
                    r_h = height[r]
                    total_water += r_w
                    r_w = 0
            else:
                l+=1
                if l_h > height[l]:
                    l_w += l_h-height[l]
                else:
                    l_h = height[l]
                    total_water+=l_w
                    l_w = 0
        return total_water
            
            
