class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        highest_frequency = max(counter.values())
        commons = counter.most_common(k)
        return [val[0] for val in commons]
        