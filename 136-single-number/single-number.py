class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        n=len(nums)
        for i in range(n):
            x=x^nums[i]
        return x
        