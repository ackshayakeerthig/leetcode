class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        d={0:0,1:0,2:0}
        for i , val in enumerate(nums):
            d[val]+=1
        keys=d.keys()
        keys.sort()
        j=0
        i=0
        while (i<len(nums)):
            if d[keys[j]]<=0:
                j+=1
                continue
            nums[i]=keys[j]
            d[keys[j]]-=1
            i+=1
        return nums

        