class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        depth=0
        for char in s:
            if char=='(':
                depth+=1
            elif char==")":
                if depth>maxi:
                    maxi=depth
                depth-=1
        return maxi
        