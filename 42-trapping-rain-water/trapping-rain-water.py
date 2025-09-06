class Solution(object):
    def trap(self, arr):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(arr)
        lmax=arr[0]
        rmax=arr[n-1]
        l=0
        r=n-1
        total=0
        while l<r:
            if arr[l]<=arr[r]:
                if arr[l]<lmax:
                    total+=lmax-arr[l]
                else:
                    lmax=arr[l]
                l+=1
            else:
                if arr[r]<rmax:
                    total+=rmax-arr[r]
                else:
                    rmax=arr[r]
                r-=1
        return total
