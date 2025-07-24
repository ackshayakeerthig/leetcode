class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        i=0
        while (i<len(nums)):
            count=0
            while (i<len(nums) and nums[i]==1  ):
                i+=1
                count+=1
            if count>max:
                max=count
            i+=1
        return max