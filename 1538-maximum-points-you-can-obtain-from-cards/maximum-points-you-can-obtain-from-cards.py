class Solution:
    def maxScore(self, cards: List[int], k: int) -> int:
        lsum=sum(cards[:k])
        rsum=0
        n=len(cards)
        maxi=lsum
        for i in range(0,k):
            lsum-=cards[k-i-1]
            rsum+=cards[n-1-i]
            maxi=max(maxi,lsum+rsum)
        return maxi