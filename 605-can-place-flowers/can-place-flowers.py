class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], plants: int) -> bool:
        n=len(flowerbed)
        if n==0:
            return False
        if n==1:
            if flowerbed[0]==0:
                return True if plants<=1 else False
            return False if plants!=0 else True
        for i in range(n):
            if flowerbed[i]==0:
                left=i-1
                right=i+1
                if 0<=left<n and 0<=right<n and flowerbed[left]==0 and flowerbed[right]==0:
                    flowerbed[i]=1
                    plants-=1
                elif i==0:
                    if  flowerbed[right]==0:
                        flowerbed[i]=1
                        plants-=1
                elif  i==n-1:
                    if  flowerbed[left]==0:
                        flowerbed[i]=1
                        plants-=1
                
        return True if plants<=0 else False