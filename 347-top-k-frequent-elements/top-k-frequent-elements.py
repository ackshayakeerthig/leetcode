class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        h=[]
        for key,val in freq.items():
            heapq.heappush(h,(-val,key))
        answer=[]
        for i in range(min(k,len(freq))):
            answer.append(heapq.heappop(h)[1])
        return answer
