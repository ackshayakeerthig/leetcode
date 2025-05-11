class Solution:
    def smallestNumber(self, n: int) -> int:
        x=1
        while (n//2!=0):
            x=x*2+1
            n=n//2
        return x
        