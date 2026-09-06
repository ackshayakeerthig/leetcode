class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        n=len(nums)
        while left<right:
            mid=(left+right)//2
            if mid%2==1:
                mid-=1
            if mid+1<n and nums[mid]==nums[mid+1]:
                left=mid+2
            else:
                right=mid
        return nums[left]