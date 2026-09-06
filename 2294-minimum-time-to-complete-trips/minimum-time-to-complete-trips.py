class Solution:
    def minimumTime(self, times: List[int], totalTrips: int) -> int:
        low=1
        high=min(times)*totalTrips
        def completes(t):
            ans=0
            for time in times:
                ans+=t//time
                if ans>=totalTrips:
                    return True
            return False
        while low<high:
            mid=(low+high)//2
            if completes(mid):
                high=mid
            else:
                low=mid+1
        return low