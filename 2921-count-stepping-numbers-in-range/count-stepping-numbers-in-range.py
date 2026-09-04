class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD=10**9+7
        def smaller_len_counts(s):
            n=len(s)
            ans=0
            dp=[[0]*10 for _ in range(n+1)]
            for i in range(1,10):
                dp[1][i]=1
            for length in range(2,n+1):
                for digit in range(10):
                    if digit-1>=0:
                        dp[length][digit]+=dp[length-1][digit-1]
                    if digit+1<=9:
                        dp[length][digit]+=dp[length-1][digit+1]
                    dp[length][digit] %= MOD
            for length in range(1,n):
                ans+=sum(dp[length])

            return ans
        def same_len_counts(s):
            #bottom up
            n=len(s)
            dp=[[[0]*2 for prev in range(10)] for _ in range(n+1)]
            for prev in range(10):
                dp[n][prev][0]=1
                dp[n][prev][1]=1
            for pos in range(n-1,0,-1):
                for cur in range(10):
                    #not tight
                    if cur-1>=0:
                        dp[pos][cur][0]+=dp[pos+1][cur-1][0]
                    if cur+1<=9:
                        dp[pos][cur][0]+=dp[pos+1][cur+1][0]
                    #tight
                    limit=int(s[pos])
                    if cur+1<=9 and cur+1<=limit:
                        dp[pos][cur][1]+=dp[pos+1][cur+1][int(cur+1==limit)]
                    if cur-1>=0 and cur-1<=limit:
                        dp[pos][cur][1]+=dp[pos+1][cur-1][int(cur-1==limit)]
            #handling first digit separately
            ans=0
            first_digit=int(s[0])
            for first in range(1,first_digit+1):
                ans+=dp[1][first][int(first==first_digit)]
                ans%=MOD
            return ans

        ans=0
        ans= (smaller_len_counts(high)-smaller_len_counts(low)+same_len_counts(high)-same_len_counts(low))%MOD
        for i in range(len(low)-1):
            if abs(int(low[i])-int(low[i+1]))!=1:
                break
        else:
            ans+=1
        return ans%MOD