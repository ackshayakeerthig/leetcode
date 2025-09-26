class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        dp=[[[-1]*3 for _ in range(2)] for _ in range(n+1)]
        for index in range(n):
            for buy in range(2):
                dp[index][buy][0]=0
        
        for buy in range(2):
            for cap in range(3):
                dp[n][buy][cap]=0
        for index in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    if buy==1:
                        profit=max(dp[index+1][0][cap]-prices[index],dp[index+1][1][cap])
                    else:
                        profit=max(dp[index+1][1][cap-1]+prices[index],dp[index+1][0][cap])
                    dp[index][buy][cap]=profit
        return dp[0][1][2]