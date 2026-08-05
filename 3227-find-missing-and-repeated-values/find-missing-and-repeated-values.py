class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        n=n*n
        expected_sum=n*(n+1)//2
        expected_square_sum=n*(n+1)*(2*n+1)//6
        actual_sum=0
        actual_square_sum=0
        for numlist in grid:
            for num in numlist:
                actual_sum+=num
                actual_square_sum+=num*num
        S=actual_square_sum-expected_square_sum
        D=actual_sum-expected_sum
        a = (D + S // D) // 2
        b = (S // D - D) // 2

        return [a, b]