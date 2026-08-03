class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for char in s:
            if char=='*' and len(ans)>0:
                ans.pop()
            else:
                ans.append(char)
        return "".join(ans)

        