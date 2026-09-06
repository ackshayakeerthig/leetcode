class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        def caneat(k):
            consumed_hrs=0
            for pile in piles:
                consumed_hrs+=ceil((pile)/k)
                if consumed_hrs>h:
                    return False
            return True
        while low<high:
            mid=(low+high)//2
            if caneat(mid):
                high=mid
            else:
                low=mid+1
        return low