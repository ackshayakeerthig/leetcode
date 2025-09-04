class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        result=[]
        result.append(intervals[0])
        for start,end in intervals:
            i_start=result[-1][0]
            i_end=result[-1][1]
            if start > i_end:
                result.append([start,end])
            else:
                result[-1]=[i_start,max(i_end, end)]
        return result
        