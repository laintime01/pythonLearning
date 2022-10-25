# leetcode 3 longestSubstring

class Solution(object):
    def longestSub(self, s):
        dic = {}
        i, ans = -1, 0
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            ans = max(ans, j-i)
            dic[s[j]] = j
        print(ans)
        return ans


# test
s_list = ["pwwkew", "bbbbb","abcabcbb"]
solution = Solution()
for s in s_list:
    solution.longestSub(s)