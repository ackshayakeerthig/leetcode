class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]

        def find(i,buy):
            if i==n:
                return 0
            if dp[i][buy]==-1:
                if buy:
                    profit=max(find(i+1,0)-prices[i],find(i+1,1))
                else:
                    profit=max(find(i+1,1)+prices[i],find(i+1,0))
                dp[i][buy]=profit
            return dp[i][buy]
        return find(0,1)