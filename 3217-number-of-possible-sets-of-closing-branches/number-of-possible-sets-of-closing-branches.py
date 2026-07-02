class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        def compute_floyd_warshall(nodes):
            matrix=[[0 if i==j   else float('inf') for j in range(n)] for i in range(n)]
            # and i not in nodes and j not in nodes
            for u,v,w in roads:
                # if u not in nodes or v not in nodes:
                #     continue
                matrix[u][v]=min(w,matrix[u][v])
                matrix[v][u]=min(w,matrix[v][u])
            for k in nodes:
                for i in nodes:
                    for j in nodes:
                        new_dist=matrix[i][k]+matrix[k][j]
                        if new_dist>maxDistance:
                            continue
                        matrix[i][j]=min(matrix[i][j],new_dist)
            for i in nodes:
                for j in nodes:
                    if matrix[i][j]>maxDistance :
                        return False
            return True
        combis=0
        for mask in range(2**n):
            nodes_combi=[]
            for i in range(n):
                if (mask>>i)%2==1:
                    nodes_combi.append(i)
            # print(nodes_combi)
            if compute_floyd_warshall(nodes_combi):
                combis+=1
                # print(combis)
        return combis