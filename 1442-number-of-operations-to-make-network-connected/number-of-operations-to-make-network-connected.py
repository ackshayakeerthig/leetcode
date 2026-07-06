class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        parent=[i for i in range(n)]
        rank=[0]*n
        unnecessary_edges=0
        def findparent(x):
            if parent[x]!=x:
                parent[x]=findparent(parent[x])
            return parent[x]
        def union_by_rank(u,v):
            ult_u=findparent(u)
            ult_v=findparent(v)
            nonlocal unnecessary_edges
            if ult_u==ult_v:
                unnecessary_edges+=1
                return
            elif rank[ult_u]<rank[ult_v]:
                parent[ult_u]=ult_v
            elif rank[ult_u]>rank[ult_v]:
                parent[ult_v]=ult_u
            else:
                parent[ult_u]=ult_v
                rank[ult_v]+=1
        for src,dest in connections:
            union_by_rank(src,dest)
        components=0
        for i in range(n):
            if findparent(i)==i:
                components+=1
        if unnecessary_edges>=components-1:
            return components-1
        return -1