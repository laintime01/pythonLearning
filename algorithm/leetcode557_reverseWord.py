# leetcode 557 reverse word

class Solution(object):
    def reverseWord(self, s):
        ps = s.split()
        st = ""
        for i in ps:
            st += i[::-1] + " "
        return st[:-1]



# test
expect_result = "s'teL ekat edoCteeL tsetnoc"
string_ = "Let's take LeetCode contest"
solu = Solution()
print(expect_result)
print(solu.reverseWord(string_))
