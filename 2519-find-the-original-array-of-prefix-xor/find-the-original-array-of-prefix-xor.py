class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n=len(pref)
        ans=[]
        prev=0
        for i in range(n):
            ans.append(prev^pref[i])
            prev=pref[i]
        return ans