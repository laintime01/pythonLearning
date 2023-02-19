class Solution(object):
    def longestPalindrome(self, words):
        """
        :param words: List[str]
        :return:int
        """

        def get_num(first, second):
            return (ord(first) - 97) * 26 + ord(second) - 97

        mid_cnt = 0
        res = 0
        num_dict = {}
        for word in words:
            if word[0] == word[1]:
                mid_flag = True
            else:
                mid_flag = False

            reverse_num = get_num(word[1], word[0])
            if num_dict.get(reverse_num, 0) > 0:
                res += 4
                num_dict[reverse_num] -= 1
                if mid_flag:
                    mid_cnt -= 1
            else:
                num = get_num(word[0], word[1])
                num_dict[num] = num_dict.get(num, 0) + 1
                if mid_flag:
                    mid_cnt += 1

        if mid_cnt > 0:
            res += 2

        print(res)
        return res


words = ["lc", "cl", "gg"]
Solution().longestPalindrome(words)
