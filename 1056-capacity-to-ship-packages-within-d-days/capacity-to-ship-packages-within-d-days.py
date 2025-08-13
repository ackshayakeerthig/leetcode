class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_weight=sum(weights)
        n=len(weights)
        def loadable(capacity):
            day=1
            load=0
            for weight in weights:
                if weight+load>capacity:
                    day+=1
                    load=weight
                else:
                    load+=weight
            return day
        low=max(weights)
        high=total_weight
        ans=None
        while low<=high:
            mid=(low+high)//2
            if loadable(mid)<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
                