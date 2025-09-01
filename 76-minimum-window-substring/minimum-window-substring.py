class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minlen=float("inf")
        cnt=0
        sindex=-1
        l,r=0,0
        hash=defaultdict(int)
        for letter in t:
            hash[letter]+=1
        while r<len(s):
            if hash[s[r]]>0:
                cnt+=1
            hash[s[r]]-=1
            while cnt == len(t):
                if r-l+1<minlen:
                    minlen= r-l+1
                    sindex=l
                hash[s[l]]+=1
                if hash[s[l]]>0:
                    cnt-=1
                l+=1
            r+=1
        return s[sindex:sindex+minlen] if sindex!=-1 else ""

