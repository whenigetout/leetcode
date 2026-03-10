# Problem: 121. Best Time To Buy And Sell Stock
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: 

from typing import List, Optional

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        if len(prices) < 2:
            return 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                cur_profit = prices[r] - prices[l]
                max_profit = max(max_profit, cur_profit)
        return max_profit