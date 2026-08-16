class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = defaultdict(int)
        count=0
        for x in time:
            r=x%60
            count+=cnt[(60-r)%60]
            cnt[r]+=1
        return count