class Solution(object):
    def longest_palindrome(self, s):
        """ Given a string s which consists of lowercase or uppercase letters,
        return the length of the longest palindrome that can be built with
        those letters.
        :param s: string
        :return: int
        """
        set_s = set()
        length = 0
        for i in s:
            if i in set_s:
                print(i)
                set_s.remove(i)
                length += 2
                print(length)
            else:
                set_s.add(i)
                print(length)
        if len(set_s) > 0:
            length += 1
        return length

str = "abccccdd"
solu = Solution()
solu.longest_palindrome(str)