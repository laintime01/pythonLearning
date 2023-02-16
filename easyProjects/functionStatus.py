import re


# 第一种办法 用闭包函数
def make_cyclic_mosaic():
    chars = ['*', 'x']
    _index = 0

    def _mosaic(strs):
        nonlocal _index
        _char = chars[_index]
        _index = (_index + 1) % len(chars)
        length = len(strs.group())
        return _char * length

    return _mosaic


t = "商店有100个苹果，小明以12元每斤的价格买走了8个。"
print(re.sub(r'\d+', make_cyclic_mosaic(), t))

# 第二种办法 用类
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
