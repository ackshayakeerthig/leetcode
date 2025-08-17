class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x:x[1])
        dp=[(0,0)]
        for j in range(len(rides)):
            start,end,tip=rides[j]
            i=bisect.bisect_right(dp,start,key=lambda x :x[0])
            prev_earning=dp[i-1][1]
            next_earning=prev_earning+end-start+tip
            if next_earning > dp[-1][1]:
                dp.append((end,next_earning))
            else:
                dp.append(dp[-1])
        return dp[-1][1]
            