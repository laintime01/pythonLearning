class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        short = min(strs, key=len)
        for i, ch in enumerate(short):
            for others in strs:
                if others[i] != ch:
                    return short[:i]
        return short


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
