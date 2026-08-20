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
                    # print(f"added water to r_w: {r_w}")
                else:
                    r_h = height[r]
                    total_water += r_w
                    r_w = 0
                    # print(f"updated water in total from r: {total_water}")
            else:
                l+=1
                if l_h > height[l]:
                    l_w += l_h-height[l]
                    # print(f"added water to l_w: {l_w}")
                else:
                    l_h = height[l]
                    total_water+=l_w
                    l_w = 0
                    # print(f"updated water in total from l: {total_water}")
        # print(f"Amount left: total_water: {total_water}, l,l_h,l_w: {l},{l_h},{l_w}, r,r_h,r_w: {r},{r_h},{r_w}")
        return total_water
            
            
