class Solution(object):
    def decodeStr(self, s):
        """
        :param s: str
        :return: str
        """
        stack, multi, res = [], 0, ''
        for w in s:
            if w.isdigit():
                multi = multi*10 + int(w)
            elif w == '[':
                stack.append([res, multi])
                res = ''
                multi = 0
            elif w == ']':
                pre_res, pre_multi = stack.pop()
                res = pre_res + res*pre_multi
            else:
                res += w
        return res



print(Solution().decodeStr("3[a]2[bc]"))
