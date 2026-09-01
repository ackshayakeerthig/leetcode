class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rank=[0]*26
        parent=[i for i in range(26)]

        def find_parent(node):
            if parent[node]!=node:
                parent[node]=find_parent(parent[node])
            return parent[node]
        def union(a,b):
            parent_a=find_parent(a)
            parent_b=find_parent(b)
            if parent_a==parent_b:
                return
            if parent_a>parent_b:
                parent[parent_a]=parent_b
            else:
                parent[parent_b]=parent_a
        for char1,char2 in zip(s1,s2):
            union(ord(char1)-ord('a'),ord(char2)-ord('a'))
        ans=""
        for char in baseStr:
            parent_char_no=find_parent(ord(char)-ord('a'))
            # mini=ord(char)-ord('a')
            # # for i in range(ord(char)-ord('a')):
            # for i in range(26):
            #     if find_parent(i)==parent_char_no :
            #         mini=min(i,mini)
            # ans=ans+chr((mini+ord('a')))
            ans=ans+chr((parent_char_no+ord('a')))
        return ans