class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrix=[[float('inf')]*numCourses for i in range(numCourses)]
        for source,dest in prerequisites:
            matrix[source][dest]=1
        for i in range(numCourses):
            matrix[i][i]=0
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    matrix[i][j]=1 if (matrix[i][j]==1 or matrix[i][k]==1 and matrix[k][j]==1) else 0
        answer=[]
        for u,v in queries:
            answer.append(True if matrix[u][v]==1 else False)
        return answer