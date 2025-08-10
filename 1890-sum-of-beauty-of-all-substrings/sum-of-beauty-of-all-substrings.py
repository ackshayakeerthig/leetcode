class Solution:
    def beautySum(self, s: str) -> int:
        summ=0
        n=len(s)
        for i in range(n):
            freq=Counter()
            for j in range(i,n):
                freq[s[j]]+=1
                maxi=max(freq.values())
                mini=min(freq.values())
                summ+=maxi-mini
        return summ