class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totals = [1]*len(nums)
        right = len(nums)-1
        left = 0
        
        cur_left = 1
        cur_right = 1
        while left < len(nums):
            totals[left] = cur_left*totals[left]
            totals[right] = cur_right*totals[right]

            cur_left *= nums[left]
            cur_right *= nums[right]

            left += 1
            right -= 1


        return totals
        