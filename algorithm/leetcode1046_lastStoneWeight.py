import heapq


class Solution(object):
    def lastStone(self, stones):
        """
        :param stones:List[int]
        :return:int
        """
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            num1 = -heapq.heappop(heap)
            num2 = -heapq.heappop(heap)
            num1 -= num2
            if num1 > 0:
                heapq.heappush(heap, -num1)

        if not heap:
            return 0
        return -heap[0]


test_stones = [2, 7, 4, 1, 8, 1]
print(Solution().lastStone(test_stones))
