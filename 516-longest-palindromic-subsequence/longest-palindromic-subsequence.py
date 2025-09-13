class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        rs=s[::-1]
        dp=[[0]*(len(s)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0]=dp[0][i]=0
        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                if s[i-1]==rs[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[len(s)][len(s)]
        