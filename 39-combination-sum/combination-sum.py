class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        def backtrack(answer,cur_array,summ,i):
            if i>=n:
                if summ==target:
                    answer.append(cur_array)
                return 
            if summ+candidates[i]==target:
                answer.append(cur_array+[candidates[i]])
            elif summ+candidates[i]<target:
                backtrack(answer,cur_array+[candidates[i]],summ+candidates[i],i)
                backtrack(answer,cur_array,summ,i+1)
            return 
        answer=[]
        candidates.sort()
        backtrack(answer,[],0,0)
        return answer