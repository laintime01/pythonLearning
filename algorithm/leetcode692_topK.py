import heapq
from collections import Counter


class Solution(object):
    def topK(self, words, k):
        """
        :param words:List[str]
        :param k:int
        :return:List[str]
        """
        counter = Counter(words)

        top = []

        # 将当前字符串及其出现次数放入 top 中
        for word, cnt in counter.items():
            heapq.heappush(top, (cnt, word))
            print(top)
            # 保持 top 只有前 k 个出现次数最多的
            if len(top) > k:
                heapq.heappop(top)

        ans = []
        while top:
            ans.append(heapq.heappop(top)[1])

        # ans 的顺序是次数少的在前，所以要反向
        # ans.reverse()
        return ans


class ReverseStr:
    def __init__(self, s):
        self.s = s

    def __lt__(self, other):
        return self.s > other.s

    def __eq__(self, other):
        return self.s == other.s


words = ["the","day","is","sunny","the","the","the","sunny","is","is"]


print(Solution().topK(words, 2))
