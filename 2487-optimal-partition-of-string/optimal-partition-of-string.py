class Solution:
    def partitionString(self, s: str) -> int:
        cnt=1
        mask=0
        for i in range(len(s)):
            if mask & (1<<ord(s[i])):
                mask=1<<ord(s[i])
                cnt+=1
            else:
                mask|=1<<ord(s[i])
        return cnt
