class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]-stones[0]!=1:
            return False
        dp=[[False]*len(stones) for i in range(len(stones))]
        return self.find(stones, 0, 1, dp)
    def find(self, stones:list, lastindex:int, currentindex:int, dp:list[list]):
        if currentindex==len(stones)-1:
            return True
        if dp[lastindex][currentindex]:
            return False
        nextindex=currentindex+1
        lastjump=stones[currentindex]-stones[lastindex]
        while nextindex<len(stones) and stones[nextindex]<=stones[currentindex]+lastjump+1:
            newjump=stones[nextindex]-stones[currentindex]
            jump=newjump-lastjump
            if jump>=-1 and jump<=1:
                if self.find(stones,currentindex,nextindex,dp):
                    return True
            nextindex+=1
        dp[lastindex][currentindex]=True
        return False