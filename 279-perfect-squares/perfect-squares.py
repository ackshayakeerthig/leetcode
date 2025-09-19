class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[n]*(n+1)
        dp[0]=0
        for num in range(1,n+1):
            i=1
            while i*i<=num:
                dp[num]=min(1+dp[num-i*i],dp[num])
                i+=1
        return dp[-1]
