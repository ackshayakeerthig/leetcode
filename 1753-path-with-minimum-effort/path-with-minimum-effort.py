class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dist=[[float('inf')]*cols for  _ in range(rows)]
        if rows>0 and cols>0:
            dist[0][0]=0
        hp=[]
        # heapq.heappush(hp,(grid[0][0],0,0))
        heapq.heappush(hp,(0,0,0))
        adj=[(-1,0),(1,0),(0,-1),(0,1)]
        while hp:
            distance,x_current,y_current=heapq.heappop(hp)
            if (x_current,y_current)>=(rows-1,cols-1):
                return dist[x_current][y_current]
            for x_add,y_add in adj:
                x_neigh,y_neigh=x_current+x_add,y_current+y_add
                # if 0<=x_neigh<rows and 0<=y_neigh<cols and dist[x_neigh][y_neigh]>abs(grid[x_current][y_current]-grid[x_neigh][y_neigh]):
                if 0<=x_neigh<rows and 0<=y_neigh<cols :
                    edge_cost=abs(grid[x_neigh][y_neigh]-grid[x_current][y_current])
                    new_effort=max(distance,edge_cost)
                    if new_effort<dist[x_neigh][y_neigh]:
                        dist[x_neigh][y_neigh]=new_effort
                        heapq.heappush(hp,(new_effort,x_neigh,y_neigh))
                        
                    # dist[x_neigh][y_neigh]=abs(grid[x_current][y_current]-grid[x_neigh][y_neigh])
                    # heapq.heappush(hp,(dist[x_neigh][y_neigh],x_neigh,y_neigh))
        return -1
