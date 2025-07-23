class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp=[[-1]*(len(text2)+1) for _ in range(len(text1)+1)]
        self.f(text1,text2,len(text1)-1,len(text2)-1,dp)
        return dp[len(text1)][len(text2)]
    def f(self,text1,text2,i1,i2,dp):
        if dp[i1+1][i2+1]==-1:
            if i1<0 or i2<0:
                 dp[i1+1][i2+1]=0
            elif text1[i1]==text2[i2]:
                dp[i1+1][i2+1]=1+self.f(text1,text2,i1-1,i2-1,dp)
            else:
                dp[i1+1][i2+1]=max(self.f(text1,text2,i1,i2-1,dp),self.f(text1,text2,i1-1,i2,dp))
        return dp[i1+1][i2+1]
        
        
        