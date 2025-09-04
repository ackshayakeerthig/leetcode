class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        summ=1
        i=1
        while i<n:
            if ratings[i]==ratings[i-1]:
                summ+=1
                i+=1
            peak=1
            while i< n and ratings[i]>ratings[i-1]:
                peak+=1
                summ+=peak
                i+=1
            down=0
            while i< n and ratings[i] <ratings[i-1]:
                down+=1
                summ+=down
                i+=1
            down+=1
            if down > peak:
                summ+=down-peak
        return summ