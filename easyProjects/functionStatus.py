import re


class CyclicMosaic:
    chars = ['*', 'x']

    def __init__(self):
        self._char_index = 0

    def generate(self, matchobj):
        char = self.chars[self._char_index]
        self._char_index = (self._char_index + 1) % len(self.chars)
        length = len(matchobj.group())
        return char * length


def handle_strs(strs):
    return re.sub(r'\d+', CyclicMosaic().generate, strs)


s = "商店有100个苹果，小明以12元每斤的价格买走了8个。"
print(handle_strs(s))
