import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # Python has min heap, so use negative values for max heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)  # largest
            x = -heapq.heappop(stones)  # second largest

            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0