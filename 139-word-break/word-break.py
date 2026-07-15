class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)
        n=len(s)
        dp=[-1]*(n+1)
        dp[0]=1
        maxlen = max(map(lambda x: len(x), wordDict))
        for i in range(n+1):
            for j in range(i,max(i-maxlen,0),-1):
                if dp[i]==-1:
                    if s[j-1:i] in wordDict and dp[j-1]==1:
                        dp[i]=1
            if dp[i]==-1:
                dp[i]=0
        return dp[n]==1
