#  RUNTIME: 16ms (beats 84.28%)  MEMORY: 11.60MB (beats 100.00%)
# [ Time taken: 11 m 50 s ]
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest_candie = max(candies)
        for index, candie in enumerate(candies):
            candies[index] = True if candie + extraCandies >= greatest_candie else False
        return candies
