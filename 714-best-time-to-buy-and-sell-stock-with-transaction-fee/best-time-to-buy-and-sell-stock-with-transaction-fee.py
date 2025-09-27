class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n=len(prices)
        after=[0]*2
        cur=[0]*2
        for i in range(n-1,-1,-1):
            cur[1]=max(after[0]-prices[i],after[1])
            cur[0]=max(after[1]+prices[i]-fee,after[0])
            after,cur=cur,after
        return after[1]
        