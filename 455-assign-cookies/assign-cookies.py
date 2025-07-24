class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        d={}
        for i,val in enumerate(set(s)):
            d[val]=s.count(val)
        count=0
        g.sort(reverse=True)
        keys=d.keys()
        keys.sort(reverse=True)
        for i in range(len(g)):
            if len(keys)<=0:
                return count
            key=keys[0]
            if g[i]<=key:
                count+=1
                d[key]-=1
                if d[key]<=0:
                    del d[key]
                    del keys[0]
        return count
            


        