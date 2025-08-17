class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        start=0
        summ=0
        if sum(gas)<sum(cost):
            return -1
        for i in range(n):
            summ+=gas[i]-cost[i]
            if summ<0:
                start=i+1
                summ=0
        return start
                