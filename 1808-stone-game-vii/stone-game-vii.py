class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n=len(stones)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+stones[i]
        total=prefix[n]
        dp=[[0]*(n+1) for _ in range(n+1)]
        for left in range(n-1,-1,-1):
            for right in range(left+1,n):
                dp[left][right]=max(
                    prefix[right+1]-prefix[left+1]-dp[left+1][right],
                    prefix[right]-prefix[left]-dp[left][right-1]
                    ) #take left, take right
        return dp[0][n-1]