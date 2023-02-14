class Solution(object):
    def multiplyStrings(self, num1, num2):
        """
        :param num1:int
        :param num2:int
        :return:string
        """
        # 翻转数组，因为我们用第0位表示个位
        arr1 = [ord(i) - ord('0') for i in num1][::-1]
        arr2 = [ord(i) - ord('0') for i in num2][::-1]

        n, m = len(arr1), len(arr2)
        ret = [0 for i in range(n + m + 1)]
        print(ret)
        for i in range(n):
            for j in range(m):
                # 按位相乘，计算进位
                ret[i + j] += arr1[i] * arr2[j]
                print(ret)
                if ret[i + j] >= 10:
                    ret[i + j + 1] += ret[i + j] // 10
                    ret[i + j] %= 10

        # 最后把数组再转化成字符串返回,去除前面的0
        res = ''.join(map(str, ret))[::-1].lstrip('0')
        return res if len(res) > 0 else '0'


num01 = "123"
num02 = "456"

print(Solution().multiplyStrings(num01, num02))
