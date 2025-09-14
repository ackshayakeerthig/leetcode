class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq=Counter(nums)
        # max_heap=[(-count,num) for num, count in freq.items()]
        # heapq.heapify(max_heap)
        return heapq.nlargest(k,freq.keys(),key=lambda x: freq[x])
        
