class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # def find_winner(alice_stones,bob_stones, chance, present_piles):
        #     #nothing left
        #     if not present_piles:
        #         return alice_stones>bob_stones
        #     #take beginning
        #     begining=find_winner(alice_stones+present_piles[0],bob_stones,not chance,present_piles[1:]) if chance else find_winner(alice_stones,bob_stones +present_piles[0],not chance, present_piles[1:])
        #     #take end
        #     ending=find_winner(alice_stones+present_piles[-1],bob_stones,not chance,present_piles[:-1]) if chance else find_winner(alice_stones,bob_stones +present_piles[-1],not chance, present_piles[:-1])
        #     return begining or ending
        # return find_winner(0,0,True,piles)

        n=len(piles)
        memo={}
        def find(i,j):
            if i==j:
                return piles[i]
            if (i,j) in memo:
                return memo[(i,j)]
            beginning=piles[i]-find(i+1,j)
            ending=piles[j]-find(i,j-1)
            memo[(i,j)]=max(beginning,ending)
            return memo[(i,j)]
        return find(0,n-1)>0