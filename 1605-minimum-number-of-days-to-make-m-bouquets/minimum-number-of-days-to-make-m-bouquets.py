class Solution:
    def minDays(self, bloomday: List[int], m: int, k: int) -> int:
        n=len(bloomday)
        required=m*k
        if n<required:
            return -1
        def bouquets(day):
            count=0
            total=0
            for dayi in bloomday:
                if dayi<=day:
                    count+=1
                else:
                    total+=(count//k)
                    count=0
            total+=(count//k)
            return total>=m
        low=bloomday[0]
        high=bloomday[0]
        for day in bloomday:
            if day<low:
                low=day
            elif day>high:
                high=day
        ans=None
        while (low<=high):
            mid=(low+high)//2
            possible=bouquets(mid)
            if possible:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
