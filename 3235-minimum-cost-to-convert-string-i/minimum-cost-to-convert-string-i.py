class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        matrix=[[float('inf') if j!=i  else 0 for j in range(26)] for i in range(26)]
        for i,(u,v,d) in enumerate(zip(original,changed,cost)):
            matrix[ord(u)-ord('a')][ord(v)-ord('a')]=min(d,matrix[ord(u)-ord('a')][ord(v)-ord('a')])
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
        total_cost=0
        for i in range(len(source)):
            u=ord(source[i])-ord('a')
            v=ord(target[i])-ord('a')
            if matrix[u][v]==float('inf'):
                return -1
            total_cost+=matrix[u][v] 
        return total_cost