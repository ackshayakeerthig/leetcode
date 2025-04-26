class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        n=len(nums1)
        for i in range(0,n):
            if nums1[i] in nums2:
                found=nums2.index(nums1[i])
                if found==len(nums2)-1:
                    ans.append(-1)
                else:
                    flag=0
                    for j in range(found+1,len(nums2)):
                        if (nums2[j]>nums1[i]):
                            ans.append(nums2[j])
                            flag=1
                            break
                    if not flag:
                        ans.append(-1)
        return ans
                