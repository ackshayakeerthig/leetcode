
def rle_encode(istring:str):
    count=1
    prev=istring[0]
    ostring=""
    for i in range(1,len(istring)):
        cur=istring[i]
        if cur==prev:
            count+=1
        else:
            ostring=ostring+str(count)+prev
            count=1
        prev=cur
    ostring=ostring+str(count)+prev
    return ostring
class Solution:
    def countAndSay(self, n: int) -> str:
        cas=["1"]
        for i in range(2,n+1):
            cas.append(rle_encode(cas[-1]))
        print(cas)
        return cas[-1]