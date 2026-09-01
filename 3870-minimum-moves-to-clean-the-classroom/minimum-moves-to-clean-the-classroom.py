class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        litterno=0
        rows=len(classroom)
        if rows<=0:
            return 0
        cols=len(classroom[0])
        q=deque()
        classroom = [list(row) for row in classroom]
        for i in range(rows):
            for j in range(cols):
                if classroom[i][j]=='S':
                    q.append((i,j,energy,0))
                elif classroom[i][j]=='L':
                    classroom[i][j]=litterno
                    litterno+=1
        visited=[[[[False]*(1<<litterno) for _ in range(energy+1)] for _ in range(cols)] for _ in range(rows)]
        visited[q[0][0]][q[0][1]][q[0][2]][q[0][3]]=True
        steps=0
        while q:
            for i in range(len(q)):
                cur_i,cur_j,cur_energy,litter_mask=q.popleft()
                if litter_mask == (1<<litterno)-1:
                    return steps
                if cur_energy==0:
                    continue
                for adj_x,adj_y in [(0,1),(0,-1),(-1,0),(1,0)]:
                    new_i,new_j=cur_i+adj_x,cur_j+adj_y
                    if not 0<=new_i<rows or not 0<=new_j<cols:
                        continue
                    if classroom[new_i][new_j]=='X':
                        continue
                    new_litter_mask=litter_mask
                    new_energy=cur_energy-1
                    if classroom[new_i][new_j]=='R':
                        new_energy=min(cur_energy+energy,energy)
                    elif isinstance(classroom[new_i][new_j],int):
                        new_litter_mask=litter_mask|(1<<classroom[new_i][new_j])
                    if not visited[new_i][new_j][new_energy][new_litter_mask]:
                        visited[new_i][new_j][new_energy][new_litter_mask]=True
                        q.append((new_i,new_j,new_energy,new_litter_mask))
            steps+=1
        return -1
                    
