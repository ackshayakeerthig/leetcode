class Solution:
    def minDeletions(self, s: str) -> int:
        freq=Counter(s)
        inv_freq=defaultdict(list)
        for char in freq:
            inv_freq[freq[char]].append(char)
        todelete=0
        for f in sorted(list(inv_freq.keys()),reverse=True):
            while len(inv_freq[f])>1:
                reduced_char=inv_freq[f].pop()
                
                for i in range(f-1,0,-1):
                    if len(inv_freq[i])==0:
                        inv_freq[i].append(reduced_char)
                        todelete+=(f-i)
                        break
                else:
                    todelete+=f
        return todelete