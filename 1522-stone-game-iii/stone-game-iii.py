class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        memo={}
        def find(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            memo[i]=float('-inf')
            for x in range(1,4):
                if i+x>n:
                    break
                opponent=find(i+x)
                current=sum(stoneValue[i:i+x])-opponent
                memo[i]=max(memo[i],current)
            return memo[i]
        winner=find(0)
        if winner>0:
            return "Alice"
        elif winner<0:
            return "Bob"
        return "Tie"