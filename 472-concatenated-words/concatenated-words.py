class Solution:
    def findAllConcatenatedWordsInADict(self, wordDict: List[str]) -> List[str]:
            wordDict=set(wordDict)
            def wordbreak(s):
                # words=wordDict-{s}
                n=len(s)
                dp=[-1]*n
                def find(i):
                    if i==len(s):
                        return 1
                    if dp[i]!=-1:
                        return dp[i]
                    # for word in words:
                    for j in range (i+1,n+1):
                        # if len(s[i:])>=len(word) and s[i:i+len(word)]==word:
                        if s[i:j] in wordDict and s[i:j]!=s:
                            if ( find(j)):
                                dp[i]=1
                                return dp[i]
                    dp[i]=0
                    return dp[i]
                return find(0)
            ans=[]
            for s in wordDict:
                if wordbreak(s)==1:
                    ans.append(s)
            return ans