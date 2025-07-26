class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ini=image[sr][sc]
        if ini==color:
            return image
        self.dfs(image,sr,sc,ini,color)
        return image
    def dfs(self,image,sr,sc,ini,color):
        image[sr][sc]=color
        adjacents=[(0,1),(1,0),(0,-1),(-1,0)]
        for drow,dcol in adjacents:
            row=sr+drow
            col=sc+dcol
            if 0<=row<len(image) and 0<=col<len(image[0]) and image[row][col]==ini:
                self.dfs(image,row,col,ini,color)
