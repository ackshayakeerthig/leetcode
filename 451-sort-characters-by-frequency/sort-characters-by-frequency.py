class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        sorted_chars = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return "".join(char * freq for char, freq in sorted_chars)