class Solution(object):
    def isHappy(self, n):
        already = set()
        while n != 1:
            total = 0
            while n > 0:
                tmp = n % 10
                total += tmp ** 2
                n //= 10
            if total in already:
                return False
            else:
                already.add(total)
            n = total
        return True

print(Solution().isHappy(2))
