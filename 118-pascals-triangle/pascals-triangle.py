class Solution:
    def generate(self, n: int) -> List[List[int]]:
        # dp=[[[0 for i in range(n+1)] for j in range(n+1)]]
        dp=[]
        self.find(dp,n, 0,0)
        return dp
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
        