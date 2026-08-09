class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[-1]*n for _ in range(n)]
        def find(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=1 if ( s[i]==s[j] and find(i+1,j-1)) else 0
            return dp[i][j]
        for i in range(n):
            dp[i][i]=1
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=1
        for i in range(n):
            for j in range(i+2,n):
                find(i,j)
        summ=0
        for i in range(n):
            for j in range(n):
                if dp[i][j]!=-1:
                    summ+=dp[i][j]
        return summ