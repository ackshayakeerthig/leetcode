class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # low=weights[0]
        # total_weight
        low=max(weights)
        total_weight=sum(weights)
        # for weight in weights:
        #     if weight>low:
        #         low=weight
        #     total_weight+=weight
        #     n+=1
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
                