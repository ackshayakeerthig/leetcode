class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        n=len(nums)
        # if k>(nums[-1]-n+1):
        #     return nums[-1]+k-(n-1)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            missing=nums[mid]-mid-1
            if missing < k:
                low=mid+1
            else:
                high=mid-1
        return low+k