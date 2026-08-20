class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        top_height = 0
        width_heights = []
        for idx, val in enumerate(heights):
            cur_height = val

            if cur_height > top_height:
                top_height = val
            
            if len(width_heights):
                temp_vals = []
                temp_vals.append([val, 1])
                start_index = 0
                while len(width_heights):
                    height, dim = width_heights.pop()
                    calc_height = height if height < val else val
                    calc_dim = dim + 1
                    total_height = calc_height * calc_dim
                    top_height = max(top_height, total_height)
                    
                    if temp_vals and temp_vals[-1][0] == calc_height:
                        temp_vals[-1][1] = max(temp_vals[-1][1], calc_dim)
                    else:
                        temp_vals.append([calc_height, calc_dim])
                width_heights = temp_vals
            else:
                width_heights.append([val, 1])

        return top_height