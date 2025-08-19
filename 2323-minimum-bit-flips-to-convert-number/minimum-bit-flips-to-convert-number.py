class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0
        while goal!=start:
            if start%2!=goal%2:
                count+=1
            start>>=1
            goal>>=1
        return count
