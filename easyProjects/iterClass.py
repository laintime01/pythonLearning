class Range7:
    """
    生成范围内包含7或者可以被7整除的数字
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return Range7Iterator(self)


class Range7Iterator:
    def __init__(self, range_obj):
        self.range_obj = range_obj
        self.current = range_obj.start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.current == self.range_obj.end:
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


# 生成器某种意义上也是迭代器
def range_7_gen(start, end):
    num = start
    while num < end:
        if num!=0 and (num % 7 == 0 or '7' in str(num)):
            yield num
        num += 1


r = Range7(0, 40)

print(tuple(r))
nums = range_7_gen(0, 40)
print(tuple(nums))

