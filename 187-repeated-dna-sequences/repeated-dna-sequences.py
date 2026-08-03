class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen,repeated=set(),set()
        for i in range(0,len(s)-9):
            cur_seq=s[i:i+10]
            if cur_seq in seen:
                repeated.add(cur_seq)
            seen.add(cur_seq)
        return list(repeated)