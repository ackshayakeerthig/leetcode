class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words=set(wordDict)
        dp={}
        def find(i):
            if i in dp:
                return dp[i]
            if i==len(s):
                return [""]
            res=[]
            for word in words:
                if len(s[i:])>=len(word) and s[i:i+len(word)]==word:
                    temp=find(i+len(word))
                    if temp:
                        for sub in temp:
                            res.append(word+" "+sub if sub else word)
            dp[i]=res
            return dp[i]
        return find(0)
        