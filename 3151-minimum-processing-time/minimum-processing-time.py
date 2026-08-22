class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        time=0
        for i in range(len(processorTime)):
            time=max(time,processorTime[i]+tasks[i*4])
        return time