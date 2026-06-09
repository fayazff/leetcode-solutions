class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float('inf')
        max_profit=0
        for i in range(len(prices)):
            buy=min(buy,prices[i])
            profit=prices[i]-buy
            max_profit=max(max_profit,profit)
        return max_profit