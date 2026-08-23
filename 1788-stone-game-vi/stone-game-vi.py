class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        benefit=[(a+b,a,b) for a,b in zip(aliceValues,bobValues)]
        benefit.sort(key=lambda x :-x[0])
        alice=0
        bob=0
        for i in range(len(aliceValues)):
            if i%2==0:
                alice+=benefit[i][1]
            else:
                bob+=benefit[i][2]
        if alice>bob:
            return 1
        elif alice<bob:
            return -1
        return 0
