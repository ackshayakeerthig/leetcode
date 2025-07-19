class Solution:
    def getRow(self, n: int) -> List[int]:
        dp=[]
        self.find(dp,n+1, 0,0)
        return dp[-1]
    def find(self,dp:List[List[int]],n:int,i:int,j:int):
        dp.append([1])
        for i in range(1,n):
            array=[]
            for j in range(len(dp[-1])+1):
                if j==0 or j==len(dp[-1]):
                    array.append(1)
                else:
                    array.append(dp[-1][j]+dp[-1][j-1])
            dp.append(array)
        