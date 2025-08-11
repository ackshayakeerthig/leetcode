class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(n)}
        indegree=[0]*n
        for course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1
        q=deque([i for i in range(n) if indegree[i]==0])
        order=[]
        while q:
            course=q.popleft()
            order.append(course)
            for adj in graph[course]:
                indegree[adj]-=1
                if indegree[adj]==0:
                    q.append(adj)
        return order if len(order)==n else []