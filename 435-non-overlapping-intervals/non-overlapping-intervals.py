class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals)==0:
            return 0
        intervals.sort(key=lambda x : x[1])
        cnt=1
        last_end=intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0]>=last_end:
                cnt+=1
                last_end=intervals[i][1]
        return len(intervals)-cnt
        