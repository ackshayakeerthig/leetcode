import numpy as np
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total=np.sum(grid)
        rows=len(grid)
        cols=len(grid[0])
        d={}
        hori=[0]*rows
        verti=[0]*cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] in d:
                    d[grid[i][j]].append((i,j))
                else:
                    d[grid[i][j]]=[(i,j)]
                hori[i]+=grid[i][j]
                verti[j]+=grid[i][j]
        top_sum=0
        for i in range(0,rows-1):
                top_sum+=hori[i]
                bottom_sum=total-top_sum
                needed=top_sum-bottom_sum
                if needed==0:
                    return True
                else:
                    for x,y in d.get(needed, []) :
                      if x<=i:
                        if i==0 and (y>0 and y<cols-1):
                            continue
                        elif cols==1 and not (x==0 or x==i):
                            continue
                        return True
                        

                needed=-needed
                for x,y in d.get(needed, []) :
                  if  x > i:
                    if i==rows-2 and (y>0 and y<cols-1):
                        continue
                    elif cols==1 and not (x==rows-1 or x==i+1):
                        continue
                    return True
        left_sum=0
        for j in range(0,cols-1):
                left_sum+=verti[j]
                right_sum=total-left_sum
                needed=left_sum-right_sum
                if needed==0:
                    return True
                else:
                    for x,y in d.get(needed, [])  :
                      if y<=j:
                        if j==0 and (x>0 and x<rows-1):
                            continue
                        elif rows==1 and not(y==0 or y==j):
                            continue
                        return True
                needed=-needed
                for x,y in d.get(needed, []) :
                  if  y > j:
                    if j==cols-2 and (x>0 and x<rows-1):
                        continue
                    elif rows==1 and not (y==cols-1 or y==j+1):
                        continue
                    return True
        return False
            