class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            x=1
			#ans=float("inf")
            while x*x<=i:
                dp[i]=min(dp[i],1+dp[i-x*x])
                x+=1
        return dp[n]
        