class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo={}
        def find(leftover):
            if leftover<=0:
                return False
            if leftover in memo:
                return memo[leftover]
            max_takes_sqrt=int(math.sqrt(leftover))
            i=1
            memo[leftover]=False
            while i<=max_takes_sqrt:
                memo[leftover]=memo[leftover] or not find(leftover-i*i)
                i=i+1
            return memo[leftover]
        return find(n)