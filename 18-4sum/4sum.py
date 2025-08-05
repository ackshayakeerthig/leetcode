class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        st=set()
        for i in range(n):
            for j in range(i+1,n):
                tempset=set()
                for k in range(j+1,n):
                    needed=target-(nums[i]+nums[j]+nums[k])
                    if needed in tempset:
                        temp=[nums[i],nums[j],nums[k],needed]
                        temp.sort()
                        st.add(tuple(temp))
                    tempset.add(nums[k])
        return list(st)



        