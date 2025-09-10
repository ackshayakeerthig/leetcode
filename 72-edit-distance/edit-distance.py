class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m=len(word1)
        n=len(word2)
        dp=[[-1]*n for _ in range(m)]
        def find(i,j):
            if i<0:
                    return j+1
            elif j<0:
                    return i+1
            elif dp[i][j]==-1:
                if word1[i]==word2[j]:
                    dp[i][j]=find(i-1,j-1)
                else:
                    dp[i][j]=1+min(find(i-1,j),find(i-1,j-1),find(i,j-1))
            return dp[i][j]
        return find(m-1,n-1)