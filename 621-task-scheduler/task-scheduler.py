class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count= Counter(tasks)
        maxheap=[-occurance for occurance in count.values()]
        print(maxheap)
        heapq.heapify(maxheap)
        time=0
        q=deque()
        while maxheap or q:
            time+=1
            if maxheap:
                cnt=1+heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                 heapq.heappush(maxheap,q.popleft()[0])
        return time