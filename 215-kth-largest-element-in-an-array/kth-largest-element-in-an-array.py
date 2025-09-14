class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=[-n for n in nums]
        heapq.heapify(nums)
        ans=0
        i=0
        while nums and i<k:
            ans=-heapq.heappop(nums)
            i+=1
        return ans
        
        