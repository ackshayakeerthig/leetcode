class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        cur=[[0]*3 for _ in range(2)] 
        after=[[0]*3 for _ in range(2)] 
        # for buy in range(2):
        #         after[buy][0]=0
        
        # for buy in range(2):
        #     for cap in range(3):
        #         after[buy][cap]=0
        for index in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    if buy==1:
                        profit=max(after[0][cap]-prices[index],after[1][cap])
                    else:
                        profit=max(after[1][cap-1]+prices[index],after[0][cap])
                    cur[buy][cap]=profit
            cur,after=after,cur
        return after[1][2]