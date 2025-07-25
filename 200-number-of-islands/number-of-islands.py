class Solution(object):
    def numIslands(self, graph):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not graph:
            return 0
        rows,cols=len(graph),len(graph[0])
        count=0
        visited=[[0]*cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and graph[row][col]=='1':
                    self.bfs(graph,visited,row,col)
                    count+=1
        return count
    def bfs(self,graph,visited,srow,scol):
        rows,cols=len(graph),len(graph[0])
        visited[srow][scol]=1
        queue=deque()
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        queue.append((srow,scol))
        while queue:
            row,col=queue.popleft()
            for drow,dcol in directions:
                checkrow=row+drow
                checkcol=col+dcol
                if checkrow>=0 and checkcol>=0 and checkrow<rows and checkcol<cols and not visited[checkrow][checkcol] and graph[checkrow][checkcol]=='1':
                    queue.append((checkrow,checkcol))
                    visited[checkrow][checkcol]=1


        