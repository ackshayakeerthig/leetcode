class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[]
        # left,right=0,len(potions)
        for num in spells:
            search=ceil(success/num)
            # pos=bisect.bisect_left(potions,search,left,right)
            pos=bisect.bisect_left(potions,search)
            valid=len(potions)-pos
            ans.append(valid)
            # left=pos
        return ans