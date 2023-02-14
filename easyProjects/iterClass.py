class SevenIter:
    """
    生成范围内包含7或者可以被7整除的数字
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.current == self.end:
                raise StopIteration
            if self.is_valid(self.current):
                ret = self.current
                self.current += 1
                return ret
            self.current += 1

    def is_valid(self, num):
        if num == 0:
            return False
        return num % 7 == 0 or '7' in str(num)


r = SevenIter(0, 40)
for n in r:
    print(n)
