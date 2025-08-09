class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=1:
            return 0
        for i in range(n):
            if i==0:
                if nums[i+1]<nums[i]:
                    return i
            if i==n-1:
                return i if nums[i-1]<nums[i] else -1
            if nums[i-1]<nums[i] and nums[i+1]<nums[i]:
                return i
        return -1