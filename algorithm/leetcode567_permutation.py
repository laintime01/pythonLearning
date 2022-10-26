# leetcode 567 Permutation in String
from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :param s1: str
        :param s2: str
        :return: bool
        """
        dic1 = Counter(s1)
        lns2 = len(s2)
        left, right = 0, len(s1) - 1
        dic2 = Counter(s2[0:right])
        while right < lns2:
            dic2[s2[right]] += 1
            if dic1 == dic2:
                return True
            dic2[s2[left]] -= 1
            if dic2[s2[left]] == 0:
                del dic2[s2[left]]
            left += 1
            right += 1
        return False

solution = Solution()
ss1 = "jk"
ss2 = "lldodqidkdjw"
print(solution.checkInclusion(ss1,ss2))
