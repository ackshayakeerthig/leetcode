class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length=len(needle)
        shifttable=dict.fromkeys(string.printable,length)
        for i in range(length-1):
            shifttable[needle[i]]=length-i-1
        h_index=length-1
        h_len=len(haystack)
        if h_len<length:
            return -1
        n_index=length-1
        while h_index<h_len:
            k=0
            while k<length and haystack[h_index-k]==needle[n_index-k]:
                k+=1
            if k==length:
                return h_index-k+1
            else:
                h_index+=shifttable[haystack[h_index]]
        return -1

            

        