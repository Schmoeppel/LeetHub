class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_idx = 0
        sell_idx = 1

        max_profit = 0

        while sell_idx < len(prices):
            profit = prices[sell_idx] - prices[buy_idx]
            if profit > max_profit:
                max_profit = profit
            if profit < 0:
                buy_idx = sell_idx
            sell_idx += 1
        
        return max_profit
            
