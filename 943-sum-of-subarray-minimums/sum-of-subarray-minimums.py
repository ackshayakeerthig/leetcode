class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        MOD = 10**9 + 7
        nsi=[0]*n
        psi=[0]*n
        nsi_stack=[]
        psi_stack=[]
        for i in range(n):
            while psi_stack and arr[i]<=arr[psi_stack[-1]]:
                psi_stack.pop()
            psi[i]=psi_stack[-1] if psi_stack else -1
            psi_stack.append(i)
            while  nsi_stack and arr[n-i-1]<arr[nsi_stack[-1]]:
                nsi_stack.pop()
            nsi[n-1-i]=nsi_stack[-1] if nsi_stack else n
            nsi_stack.append(n-i-1)
        total=0
        for i in range(n):
            next_s=nsi[i]
            prev_s=psi[i]
            total= (total + (i-prev_s)*(next_s-i)*arr[i])%MOD
        print(psi, nsi)
        return total