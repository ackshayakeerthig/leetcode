class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist=[[float('inf')]*(k+2) for _ in range(n)]
        dist[src][0]=0
        hp=[] #(cost,src,dst,steps)
        # heapq.heappush(hp,(0,src,src,0))
        heapq.heappush(hp,(0,0,src))
        while hp:
            cost,step,node=heapq.heappop(hp)
            if node==dst :
                return dist[dst][step]
            if step<=k:
                for new_fro,new_to,new_dist in flights:
                    if new_fro==node and dist[new_to][step+1]>cost+new_dist:
                        dist[new_to][step+1]=cost+new_dist
                        heapq.heappush(hp,(cost+new_dist,step+1,new_to))
        return -1