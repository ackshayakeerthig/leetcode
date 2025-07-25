class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        n=len(nums)
        j=0
        x=0
        y=0
        while  j<n:
            x=x^i
            i+=1
            y=y^nums[j]
            j+=1
        x=x^n
        return x^y
        