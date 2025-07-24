class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()
        child,cookie=0,0
        count=0
        while child<len(g) and cookie<len(s):
            if g[child]<=s[cookie]:
                count+=1
                child+=1
            cookie+=1
        return count