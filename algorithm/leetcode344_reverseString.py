# leetcode 344

class Solution(object):
    def reverseString(self,s):
        s[:] = s[::-1]
        print(s)


# test
input_s= ["H","a","n","n","a","h"]
expect_output = ["h","a","n","n","a","H"]
solution = Solution()
solution.reverseString(input_s)
print(expect_output)
