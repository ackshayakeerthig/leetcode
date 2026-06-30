class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for word in strs:
            word_tup=[0]*26
            for letter in word:
                word_tup[ord(letter)-ord('a')]+=1
            ans[tuple(word_tup)].append(word)
        answer=[]
        for key in ans.keys():
            l=[]
            for word in ans[key]:
                l.append(word)
            answer.append(l)
        return answer
