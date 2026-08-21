class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_p = 0

        for price in prices:
            if min_buy > price:
                min_buy = price
            elif max_p < price - min_buy:
                max_p = price-min_buy
            
        return max_p