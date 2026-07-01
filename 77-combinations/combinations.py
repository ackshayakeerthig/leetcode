
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[i for i in range(0,n+1)]

        def combinations(i , k_dup):
            if k_dup==0:
                return []
            if k_dup==1:
                return [[arr[j]] for j in range(i,n+1)]
            new_combi=[]
            for j in range(i,n+1):
                combis=combinations(j+1,k_dup-1)
                for combi in combis:
                    new_combi.append([arr[j]]+combi)
            return new_combi
        
        return combinations(1,k)