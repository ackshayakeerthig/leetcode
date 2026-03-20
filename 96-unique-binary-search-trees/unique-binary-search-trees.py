class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0 for i in range(n+1)]
        dp[0]=1
        if n>=1:
            dp[1]=1
        if n>=2:
            dp[2]=2
        for i in range(3,n+1):
            for j in range(0,i):
                dp[i]+=dp[i-j-1]*dp[j]
        return dp[n]
