class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 999999999999999999
        max_profit = 0
        for stock in prices:
            if stock < min_price:
                min_price = stock
            else:
                max_profit = max(max_profit, stock-min_price)
        
        return max_profit
