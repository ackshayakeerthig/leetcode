class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x:x[1])
        ride_end=[0]
        ride_earn=[0]
        for start,end,tip in rides:
            i=bisect_right(ride_end,start)-1
            earning=end-start+tip
            next_earn=ride_earn[i]+earning
            if next_earn > ride_earn[-1]:
                ride_end.append(end)
                ride_earn.append(next_earn)
        return ride_earn[-1]
        
