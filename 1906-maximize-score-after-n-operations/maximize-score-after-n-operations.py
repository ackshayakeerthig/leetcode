class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m=len(nums)
        total_ops=m//2
        size=1<<m
        dp=[0 for _ in range(1<<m)]
        # def solve(mask):
        #     ops=mask.bit_count()//2
        #     if ops>total_ops:
        #         return 0
        #     if dp[mask]==-1:
        #         score=0
        #         for i in range(m):
        #             for j in range(i+1,m):
        #                 if mask & (1<<i) or mask &( 1<<j):
        #                     continue
        #                 x,y=nums[i],nums[j]
        #                 score=max(score,(ops+1)*math.gcd(x,y)+solve(mask | (1<<i) | (1<<j)))
        #         dp[mask]=score
        #     return dp[mask]
        # return solve(0)
        for mask in range(size-1,-1,-1):
            ops=mask.bit_count()//2
            score=0
            for i in range(m):
                for j in range(i+1,m):
                    if mask & (1<<i) or mask &( 1<<j):
                        continue
                    x,y=nums[i],nums[j]
                    score=max(score,(ops+1)*math.gcd(x,y)+dp[mask | (1<<i) | (1<<j)])
            dp[mask]=score
        return dp[0]