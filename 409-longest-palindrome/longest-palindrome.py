class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for letter in s:
            if letter not in d:
                d[letter]=1
            else:
                d[letter]+=1
        odd_present=False
        summ=0
        for letter in d:
            if d[letter]%2==1:
                odd_present=True
                summ+=(d[letter]-1)
            else:
                summ+=d[letter]
        if odd_present:
            return summ+1
        return summ
