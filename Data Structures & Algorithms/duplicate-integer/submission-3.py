class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked: dict[int, bool] = {}
        for num in nums:
            if num in checked:
                return True
            checked[num] = 1
        return False