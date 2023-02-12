class Solution(object):
    def isHappy(self, n):
        already = []
        while n != 1:
            total = 0
            while n > 0:
                tmp = n % 10
                total += tmp ** 2
                n //= 10
            if total in already:
                return False
            else:
                already.append(total)
            n = total
        return True


print(Solution().isHappy(2))
