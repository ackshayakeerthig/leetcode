class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[cost[0],cost[1]]
        i=2
        while (i<len(cost)):
            dp.append(cost[i] + min(dp[i-1], dp[i-2]))
            i+=1
        return min(dp[-1],dp[-2])