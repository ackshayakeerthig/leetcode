class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        def backtrack(answer,cur_array,summ,i):
            print("entering | cur_array:",cur_array,"answer:",answer,"i:",i)
            if i>=n:
                return
            if summ+candidates[i]==target:
                answer.append(cur_array+[candidates[i]])
            elif summ+candidates[i]<target:
                backtrack(answer,cur_array+[candidates[i]],summ+candidates[i],i+1)
                i+=1
                while i<n and candidates[i]==candidates[i-1]:
                    i+=1
                backtrack(answer,cur_array,summ,i)
            return
        candidates.sort()
        answer=[]
        backtrack(answer,[],0,0)
        return answer