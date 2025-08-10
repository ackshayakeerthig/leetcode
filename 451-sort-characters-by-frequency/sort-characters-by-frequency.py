class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for letter in s:
            if letter not in d:
                d[letter]=1
            else:
                d[letter]+=1
        sorted_chars = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return "".join(char * freq for char, freq in sorted_chars)