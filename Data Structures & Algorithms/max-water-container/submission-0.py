class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0

        l = 0
        r = len(heights)-1

        while l < r:
            height = min(heights[l], heights[r])
            water_contained = height*(r-l)

            if water_contained > most_water:
                most_water = water_contained
            
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return most_water