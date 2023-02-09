from collections import defaultdict,Counter
class Solution(object):
    def charReplacement(self,s,k):
        window_count = defaultdict(int)  # 统计窗口内每个字符出现过的次数
        res, left, right, count_s = 0, 0, 0, len(s)

        max_repeat_count = 0  # 窗口内出现最多次字符的次数
        while right < count_s:
            window_count[s[right]] += 1  # 次数加一
            # 由于窗口只有 s[right] 增加了一次，那么 出现最多次字符的次数 只需要和这个字符的字符比较就可以了
            max_repeat_count = max(max_repeat_count, window_count[s[right]])  # 更新出现最多次字符的次数

            while right - left + 1 - max_repeat_count > k:  # left 向边移动
                window_count[s[left]] -= 1
                max_repeat_count = max(max_repeat_count, window_count[s[left]])
                left += 1

            res = max(res, right - left + 1)  # 窗口内的单词个数
            right += 1

        return res