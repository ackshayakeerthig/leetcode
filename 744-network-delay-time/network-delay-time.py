class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_taken=[float('inf')]*(n+1)
        hp=[] # (time,src)
        heapq.heappush(hp,(0,k))
        time_taken[k]=0
        while hp:
            t,current=heapq.heappop(hp)
            for src,target,edge_time in times:
                if src==current:
                    if time_taken[target]>t+edge_time:
                        time_taken[target]=t+edge_time
                        heapq.heappush(hp,(time_taken[target],target))
        ans= max(time_taken[1:])
        if ans<float('inf'):
            return ans
        return -1
            