class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        j=1
        n=len(nums)
        valid=[0 for _ in range(n)]
        for num in nums:
            if num>=0:
                valid[i]=num
                i+=2
            else:
                valid[j]=num
                j+=2
        return valid
        