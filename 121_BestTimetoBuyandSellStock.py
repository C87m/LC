# 121 Best Time to Buy and Sell Stock
# 利益の最大化

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            
            if max_profit < prices[i]-min_price:
                max_profit = prices[i]-min_price

        return max_profit