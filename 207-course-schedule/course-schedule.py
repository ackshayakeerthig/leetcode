class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        indegree=[0]*numCourses
        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course]+=1
        q=deque([i for i in range(numCourses) if indegree[i]==0])
        taken=0
        while q:
            course=q.popleft()
            taken+=1
            for adj in graph[course]:
                indegree[adj]-=1
                if indegree[adj]==0:
                    q.append(adj)
        return taken==numCourses