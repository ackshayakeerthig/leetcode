class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r=0,0
        maxlen=0
        d={}
        while (r<len(fruits)):
            d[fruits[r]]=r
            if len(d)>2:
                next_l=min(d.values())
                remove=fruits[next_l]
                del d[remove]
                l=next_l+1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen

            
            