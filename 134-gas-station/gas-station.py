class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        start=0
        sum_diff=0
        summ=0
        for i in range(n):
            difference=gas[i]-cost[i]
            sum_diff+=difference
            summ+=difference
            if summ<0:
                start=i+1
                summ=0
        if sum_diff>=0:
            return start
        return -1
                