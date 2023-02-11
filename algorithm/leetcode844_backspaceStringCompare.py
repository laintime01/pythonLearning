class Solution(object):
    def backspaceCompare(self,s,t):
        """
        :param s: str
        :param t: str
        :return: bool
        """
        if self.handleStr(s) == self.handleStr(t):
            return True
        return False

    def handleStr(self,s):
        temp = []
        for w in s:
            if w == "#" and not temp:
                continue
            elif w =="#":
                temp.pop()
            else:
                temp.append(w)
        return temp

print(Solution().handleStr("#a#c"))