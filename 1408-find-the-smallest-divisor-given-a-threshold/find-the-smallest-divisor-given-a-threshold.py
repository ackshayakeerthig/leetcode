class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divi(divisor):
            summ=0
            for num in nums:
                summ+=ceil(num/divisor)
            return summ
        low=1
        high=max(nums)
        ans=None
        while low<=high:
            mid=(low+high)//2
            if divi(mid)<=threshold :
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

            