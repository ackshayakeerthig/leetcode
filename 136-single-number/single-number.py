class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        for num in nums:
            x=x^num
        return x
        