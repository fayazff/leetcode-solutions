class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit1,profit2 =0,0
        transanction1, transanction2 =float('inf'),float('inf')
        for i in range(len(prices)):
            transanction1=min(transanction1,prices[i])
            profit1=max(profit1,prices[i]-transanction1)

            transanction2 = min(transanction2,prices[i]-profit1)
            profit2 = max(profit2,prices[i]-transanction2)
        return profit2
