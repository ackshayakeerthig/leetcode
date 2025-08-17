class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x:x[0])
        @lru_cache(None)
        def recurrence(index):
            if index==len(rides):
                return 0
            start,end,tip=rides[index]
            earning=end-start+tip
            next_index=bisect.bisect_left(rides,end,lo=index+1,key= lambda x: x[0])
            return max(recurrence(next_index)+earning , recurrence(index+1))
        return recurrence(0)