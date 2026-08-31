class Solution:
    def minDays(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows=len(matrix)
        cols=len(matrix[0])
        def findcomponents():
            visited=[[0]*cols for _ in range(rows)]
            def dfs(node_i,node_j):
                visited[node_i][node_j]=1
                for adj_x,adj_y in [(0,1),(0,-1),(-1,0),(1,0)]:
                    new_r,new_c=node_i+adj_x,node_j+adj_y
                    if 0<=new_r<rows and 0<=new_c<cols and matrix[new_r][new_c]==1 and not visited[new_r][new_c]:
                        dfs(new_r,new_c)
            components=0
            for i in range(rows):
                for j in range(cols):
                    if matrix[i][j]==1 and not visited[i][j]:
                        dfs(i,j)
                        components+=1
            return components
        initial_count=findcomponents()
        if initial_count!=1:
            return 0
        # removing 1 element
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==1:
                    matrix[i][j]=0
                    if findcomponents()!=1:
                        return 1
                    matrix[i][j]=1
        return 2



