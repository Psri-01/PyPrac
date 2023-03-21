class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        f = 1
        beds = 0
        for bed in flowerbed:
            if bed:
                beds += (f - 1) // 2
                f = 0
            else:
                f += 1
        beds += f // 2
        return beds >= n
