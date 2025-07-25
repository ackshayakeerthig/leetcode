class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i=0
        # n=len(nums)
        # j=0
        # x=0
        # y=0
        # while  j<n:
        #     x=x^i
        #     i+=1
        #     y=y^nums[j]
        #     j+=1
        # x=x^n
        # return x^y
        # n=len(nums)
        # necessarysum=n*(n+1)//2
        # actualsum=0
        # for i,val in enumerate(nums):
        #     actualsum+=val
        # return necessarysum-actualsum
        n=len(nums)
        return n*(n+1)//2-sum(nums)