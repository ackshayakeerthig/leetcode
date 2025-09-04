class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        result=[]
        i_start=intervals[0][0]
        i_end=intervals[0][1]
        for start,end in intervals:
            if start > i_end:
                result.append([i_start,i_end])
                i_start=start
                i_end=end
            else:
                i_start=min(i_start,start)
                i_end=max(i_end,end)
        result.append([i_start,i_end])
        return result
        