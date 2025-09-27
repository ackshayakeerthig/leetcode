class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        after1=[0]*2
        after2=[0]*2
        cur=[0]*2 
        for i in range(n-1,-1,-1):
            cur[1]=max(after1[0] - prices[i],after1[1])
            cur[0]=max(after2[1]+prices[i],after1[0])
            after2=after1[:]
            after1=cur[:]
        return after1[1]