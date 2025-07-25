class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        j=1
        k=0
        n=len(nums)
        valid=[0 for _ in range(n)]
        while k<n:
            if nums[k]>=0:
                valid[i]=nums[k]
                i+=2
            else:
                valid[j]=nums[k]
                j+=2
            k+=1
        return valid
        