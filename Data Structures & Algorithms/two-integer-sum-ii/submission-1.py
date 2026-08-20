class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        needed = {}

        for i in range(len(numbers)):
            if numbers[i] in needed:
                return [needed[numbers[i]]+1, i+1]
            
            leftover = target - numbers[i]

            needed[leftover] = i