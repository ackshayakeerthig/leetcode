class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_indice=sorted([(nums[i],i) for i in range(len(nums))])
        i=0
        n=len(nums)
        while i<n:
            j=i
            while j+1<n and nums_indice[j+1][0]-nums_indice[j][0]<=limit:
                j+=1
            indices=sorted([nums_indice[x][1] for x in range(i,j+1)])
            for x,idx in enumerate(indices):
                nums[idx]=nums_indice[i+x][0]
            i=j+1
        return nums
        