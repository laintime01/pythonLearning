class Solution(object):
    def bullsCows(self, secret, guess):
        """
        :param secret:str
        :param guess:str
        :return:str
        """
        bulls = 0
        cnt_s,cnt_g = [0]*10,[0]*10
        for m,n in zip(secret,guess):
            if m == n:
                bulls += 1
            else:
                cnt_s[int(m)] += 1
                cnt_g[int(n)] += 1
        cows = sum(min(s,g) for s,g in zip(cnt_s,cnt_g))
        return f"{bulls}A{cows}B"
