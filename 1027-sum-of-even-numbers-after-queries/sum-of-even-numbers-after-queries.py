class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum=0
        for num in nums:
            if num%2==0:
                sum+=num
        answer=[]
        for val,index in queries:
            if nums[index]%2==0:
                sum-=nums[index]
            nums[index]+=val
            if nums[index]%2==0 :
                    sum+=nums[index]
            answer.append(sum)
            # print("nums: ",nums)
            # print(answer)
        return answer
