class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.edges=edges
        matrix=[[0 if i==j else float('inf') for j in range(self.n)] for i in range(self.n)]
        for u,v,t in self.edges:
            matrix[u][v]=t
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
        # for i in range(self.n):
        #     for j in range(self.n):
        #         if matrix[i][j]==float('inf'):
        #             matrix[i][j]=-1
        self.matrix=matrix
    def addEdge(self, edge: List[int]) -> None:
        self.edges.append(edge)
        for i in range(self.n):
            for j in range(self.n):
                self.matrix[i][j]=min(self.matrix[i][j],self.matrix[i][edge[0]]+edge[2]+self.matrix[edge[1]][j])

    def shortestPath(self, node1: int, node2: int) -> int:
        
        return self.matrix[node1][node2] if self.matrix[node1][node2]!=float('inf') else -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)