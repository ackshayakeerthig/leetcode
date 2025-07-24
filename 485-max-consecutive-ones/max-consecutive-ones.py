class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                maxx=max(maxx,count)
            else:
                count=0
        return maxx