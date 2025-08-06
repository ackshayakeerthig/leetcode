class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], plants: int) -> bool:
        n = len(flowerbed)
        for i in range(n):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == n - 1) or (flowerbed[i + 1] == 0)
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    plants -= 1
                    if plants == 0:
                        return True
        return plants <= 0