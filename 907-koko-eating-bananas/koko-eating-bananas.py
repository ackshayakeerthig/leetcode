class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=None
        def timetaken(speed):
            sum=0
            for pile in piles:
                sum+=ceil(pile/speed)
            return sum
        while (low<=high):
            mid=(low+high)//2
            tt=timetaken(mid)
            # if tt==h:
            #     return mid
            if tt<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans