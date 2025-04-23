class Solution:
    def convert(self, s: str, n: int) -> str:
        if (n==1):
            return s
        final=""
        length=len(s)
        for i in range(0,length,2*(n)-2):
            final+=s[i]
        for i in range(1,n-1):
            j=i
            while (j<length):
                final+=s[j]
                j+=2*(n-i)-2
                if (j>=length):
                    break
                final+=s[j]
                j+=2*i
        for i in range(n-1,length,2*n-2):
            final+=s[i]
        return final
