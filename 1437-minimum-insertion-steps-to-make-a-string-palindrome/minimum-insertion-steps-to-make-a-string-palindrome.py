class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        rs=s[::-1]
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=dp[0][i]=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==rs[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return n-dp[n][n]

        