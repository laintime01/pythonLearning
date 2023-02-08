from collections import Counter, defaultdict


class Solitoin(object):
    def findAnagrams(self, s, p):
        """
        Given two strings s and p, return an array of all
        the start indices of p's anagrams in s. You may return
        the answer in any order.
        :param s:string
        :param p:string
        :return:List[int]
        """
        l = len(s)
        if not s or not p or len(p) > l:
            return []

        dict_p = Counter(p)
        required = len(dict_p)

        i,j = 0,0
        dict_win = defaultdict(int)
        formed = 0
        ans = []

        while j < l:
            ch = s[j]

            if ch in p:
                dict_win[ch] += 1
                if dict_win[ch] == dict_p[ch]:
                    formed += 1

                    while formed == required and i <= j:
                        ch = s[i]

                        if dict_win == dict_p:
                            ans.append(i)
                        dict_win[ch] -= 1
                        if dict_win[ch] < dict_p[ch]:
                            formed -= 1
                        i += 1
                    j += 1
                else:
                    j += 1
                    i = j
                    formed =0
                    dict_win = defaultdict(int)
            return ans
