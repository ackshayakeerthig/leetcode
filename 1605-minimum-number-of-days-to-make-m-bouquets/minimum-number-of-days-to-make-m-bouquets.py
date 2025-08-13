class Solution:
    def minDays(self, bloomday: List[int], m: int, k: int) -> int:
        n=len(bloomday)
        required=m*k
        if n<required:
            return -1
        def bouquets(day):
            count=0
            total=0
            for i in range(n):
                if bloomday[i]<=day:
                    count+=1
                else:
                    total+=(count//k)
                    count=0
            total+=(count//k)
            return True if total>=m  else False
        low,high=min(bloomday),max(bloomday)
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
