class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = defaultdict(int)
        count=0
        for x in hours:
            r=x%24
            count+=cnt[(24-r)%24]
            cnt[r]+=1
        return count