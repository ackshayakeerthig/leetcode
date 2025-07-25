class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            profit=prices[i]-mini
            if profit>maxprofit:
                maxprofit=profit
            if prices[i]<mini:
                mini=prices[i]
        return maxprofit