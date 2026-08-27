class Solution:
    def mincostToHireWorkers(self, workers_quality: List[int], minimum_wages: List[int], k: int) -> float:
        all_details=[(wage/quality,quality,wage) for wage,quality in zip(minimum_wages,workers_quality)]
        all_details.sort(key=lambda x : x[0])
        min_cost=float('inf')
        max_heap=[]
        quality_sum=0
        for ratio,quality,_ in all_details:
            heapq.heappush(max_heap,-quality)
            quality_sum+=quality

            if len(max_heap)>k:
                removed=-heapq.heappop(max_heap)
                quality_sum-=removed
            if len(max_heap)==k:
                min_cost=min(min_cost,ratio*quality_sum)
        return min_cost