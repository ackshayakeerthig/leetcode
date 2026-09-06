class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len=len(s)
        t_len=len(t)
        dp=[[0]*(t_len+1) for _ in  range(s_len+1)]
        for i in range(s_len+1):
            dp[i][0]=1
        for i in range(1,s_len+1):
            for j in range(1,t_len+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[s_len][t_len]