# leetcode 3 longestSubstring

class Solution(object):
    def longestSub(self, s):
        dic = {}
        i, ans = -1, 0  # i->start pointer  ans->max length
        for j in range(len(s)):  # j->end pointer traversal string s
            if s[j] in dic:  # if s[j] is dup in dic
                i = max(dic[s[j]], i)  # move i to max(where s[j] first appear or i)
                # print(f"i={i}")
            # print(f"j={j}")
            ans = max(ans, j - i)  # update ans, max between ans last time and j-i
            dic[s[j]] = j  # update j value
        print(ans)
        return ans


# test
s_list = ["pwwkew", "bbbbb", "abcabcbb"]
solution = Solution()
for s in s_list:
    solution.longestSub(s)

