class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = []
        for num in nums:
            if num not in checked:
                checked.append(num)
            else:
                return True
        return False