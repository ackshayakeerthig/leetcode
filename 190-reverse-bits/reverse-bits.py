class Solution:
    def reverseBits(self, n: int) -> int:
        i=31
        j=0
        ans=0
        x=0
        while (i>=0):
            x=n % 2
            n//=2
            ans=ans*2+x
            i-=1
        
        return ans