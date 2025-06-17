class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique=len(nums)
        i=1
        while i<len(nums):
            if nums[i-1]==nums[i]:
                unique-=1
                nums.pop(i)
                continue
            i+=1
        return unique