class Solution(object):
    def findCircleNum(self, graph):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited=[0]*len(graph)
        vertices=len(graph)
        count=0
        for i in range(vertices):
            if visited[i]==0:
                count+=1
                self.dfs(i,visited,graph)
        return count
    def dfs(self,i,visited,graph):
        visited[i]=1
        for j in range(len(graph)):
            if visited[j]==0 and graph[i][j] and i!=j:
                self.dfs(j,visited,graph)
    

        