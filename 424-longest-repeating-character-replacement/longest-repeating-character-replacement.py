class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash=[0]*26
        l,r=0,0
        maxlen=0
        maxfreq=0
        while r<len(s):
            letter=s[r]
            hash[ord(letter)-ord('A')]+=1
            maxfreq=max(maxfreq,hash[ord(letter)-ord('A')])
            if r-l+1 - maxfreq>k:
                hash[ord(s[l])-ord('A')]-=1
                # maxfreq=max(hash)
                l+=1
                
            if r-l+1 - maxfreq <=k:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
            