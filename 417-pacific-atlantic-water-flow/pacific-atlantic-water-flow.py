class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        answer=[]
        rows,cols=len(heights),len(heights[0])
        if rows<1 and cols<1:
            return answer
        canflow_pacific=[[0]*cols for _ in range(rows)]
        canflow_atlantic=[[0]*cols for _ in range(rows)]
        visited=[[0]*cols for _ in range(rows)]
        #Marking from top left
        q_pacific=deque()
        q_atlantic=deque()
        for i in range(cols):
                canflow_pacific[0][i]=1
                q_pacific.append((0,i,heights[0][i]))
                canflow_atlantic[rows-1][i]=2
                q_atlantic.append((rows-1,i,heights[rows-1][i]))
        for i in range(rows):
                canflow_pacific[i][0]=1
                q_pacific.append((i,0,heights[i][0]))
                canflow_atlantic[i][cols-1]=2
                q_atlantic.append((i,cols-1,heights[i][cols-1]))
        adjacents=[(0,1),(1,0),(0,-1),(-1,0)]
        while q_pacific:
            currow,curcol,curheight=q_pacific.popleft()
            visited[currow][curcol]=1
            for x,y in adjacents:
                adjrow,adjcol=x+currow,y+curcol
                if 0<=adjrow<rows and 0<=adjcol<cols and heights[adjrow][adjcol]>=curheight and not visited[adjrow][adjcol]:
                    canflow_pacific[adjrow][adjcol]=1
                    q_pacific.append((adjrow,adjcol,heights[adjrow][adjcol]))
        visited=[[0]*cols for _ in range(rows)]
        while q_atlantic:
            currow,curcol,curheight=q_atlantic.popleft()
            visited[currow][curcol]=1
            for x,y in adjacents:
                adjrow,adjcol=x+currow,y+curcol
                if 0<=adjrow<rows and 0<=adjcol<cols and heights[adjrow][adjcol]>=curheight and not visited[adjrow][adjcol]:
                    canflow_atlantic[adjrow][adjcol]=1
                    q_atlantic.append((adjrow,adjcol,heights[adjrow][adjcol]))
        for i in range(rows):
            for j in range(cols):
                if canflow_pacific[i][j] and canflow_atlantic[i][j]:
                    answer.append([i,j])
        return answer        
        # for i in range(cols-1,-1,-1):
        #     canflow[rows-1][i]=2
        # while q:
        #     currow,curcol,curheight=q.popleft()
        #     for x,y in adjacents:
        #         adjrow,adjcol=x+currow,y+curcol
        #         if 0<adjrow<rows and 0<adjcol<cols and heights[adjrow][adjcol]>=curheight  and not visited[adjrow][adjcol]:
        #             canflow[adjrow][adjcol]+=1
        #             if canflow[adjrow][adjcol]==2:
        #                 answer.append([adjrow,adjcol])
        #             q.append((adjrow,adjcol,heights[adjrow][adjcol]))
        # return answer



            
        # answer=[]
        # rows,cols=len(heights),len(heights[0])
        # if rows<1 and cols<1:
        #     return answer
        # canflow=[[0]*rows for _ in range(cols)]
        # for i in range(cols):
        #         canflow[0][i]+=1
        #         canflow[rows-1][i]+=1
        # for j in range(rows):
        #         canflow[i][0]+=1
        #         canflow[i][cols-1]+=1
        # for i in range(1,rows):
        #     for j in range(1,cols):
        #         if heights[i][j]>=heights[i][j-1] and canflow[i][j-1]>=1 or heights[i][j]>=heights[i-1][j] and canflow[i-1][j]>=1:
        #             canflow[i][j]+=1
        # for i in range(rows-2,-1,-1):
        #     for j in range(cols-2,-1,-1):
        #         if heights[i][j]>=heights[i][j+1] and canflow[i][j+1]>=1 or heights[i][j]>=heights[i+1][j] and canflow[i+1][j]>=1:
        #             canflow[i][j]+=1
        # for i in range(rows):
        #     for j in range(cols):
        #         if canflow[i][j]>=2:
        #             answer.append([i,j])
        # return answer