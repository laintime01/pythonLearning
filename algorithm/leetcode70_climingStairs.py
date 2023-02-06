class Solution(object):
    def climbStairs(self, n):
        """
        :param n: int
        :return: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 1
        cache = [1,2]
        for i in range(2, n):
            cache.append(cache[i-1] + cache[i-2])
        return cache[n-1]

print(Solution().climbStairs(38))