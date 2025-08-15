class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        def find (maxi):
            subarrays=1
            summ=0
            for num in nums:
                if summ+num<=maxi:
                    summ+=num
                else:
                    summ=num
                    subarrays+=1
                if subarrays>k:
                    return k+1
            return subarrays
        ans=None
        while (low<=high):
            mid=(low+high)//2
            subarrays=find(mid)
            if subarrays<=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans