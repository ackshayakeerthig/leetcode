class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count=0
        nums=set(nums)
        for num in nums:
            if num+diff in nums and num +2*diff in nums:
                count+=1
        return count