class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=bisect_left(nums,target)
        r=bisect_right(nums,target)-1
        if l<len(nums) and nums[l]==target:
            return [l,r]
        return [-1,-1]