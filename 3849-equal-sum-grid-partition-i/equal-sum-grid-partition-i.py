class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows=len(grid)
        cols=len(grid[0])
        hori=[sum(grid[i]) for i in range (rows)]
        verti=[0]*cols
        for i in range(rows):
            for j in range(cols):
                verti[j]+=grid[i][j]
        hori_sum=sum(hori)
        verti_sum=sum(verti)
        val=0
        for i in range(rows):
            val+=hori[i]
            hori_sum-=hori[i]
            if val==hori_sum:
                return True
        val=0
        for j in range(cols):
            val+=verti[j]
            verti_sum-=verti[j]
            if val==verti_sum:
                return True
        return False