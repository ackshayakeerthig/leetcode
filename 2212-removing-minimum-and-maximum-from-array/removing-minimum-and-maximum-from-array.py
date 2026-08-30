class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini=float('inf')
        maxi=float('-inf')
        n=len(nums)
        mini_index=0
        max_index=0
        for i in range(len(nums)):
            if nums[i]<mini:
                mini=nums[i]
                mini_index=i
            if nums[i]>maxi:
                maxi=nums[i]
                max_index=i
        
        # distance=abs(mini_index-max_index)
        # removing_both_front=min(mini_index,max_index)+1+distance
        # removing_both_back=n-1-(max(mini_index,max_index)+distance)+1
        # removing_front_back=(min(mini_index,max_index)+1)+(n-1-max(mini_index,max_index)+1)
        removing_both_front=max(mini_index,max_index)+1
        removing_both_back=n-min(mini_index,max_index)
        removing_front_back=min(mini_index,max_index)+1+n-max(mini_index,max_index)
        return min(removing_both_front,removing_both_back,removing_front_back)