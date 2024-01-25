# Definitely not the best solution.
# RUNTIME: 127ms (beats 26.34%)  MEMORY: 12.34MB (beats 95.34%)
# [ Time taken: 1 hr 16 m 58 s ]

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        for i, f in enumerate(flowerbed):
            if n == 0:
                return True
            ni = i + 1
            pi = i - 1
            nf = flowerbed[ni] if ni < l else None
            pf = flowerbed[pi]
            if i == 0 and nf == 0 and f != 1:
                n -= 1
                flowerbed[i] = 1
            elif i == l - 1 and pf == 0 and f != 1:
                n -= 1
                flowerbed[i] = 1
            elif pf == 0 and nf == 0 and f != 1:
                n -= 1
                flowerbed[i] = 1
        if n == 0:
            return True
        return False
