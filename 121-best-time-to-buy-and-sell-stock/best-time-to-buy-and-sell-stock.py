class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxprofit=0
        profit=0
        for price in prices:
            profit=price-mini
            if profit>maxprofit:
                maxprofit=profit
            if price<mini:
                mini=price
        return maxprofit