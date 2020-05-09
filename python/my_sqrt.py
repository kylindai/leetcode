from python.common.util import printCost
import math


class Solution:

    def __init__(self):
        self._a = 0

    @printCost
    def mySprt(self, x: int) -> int:
        """
        求一个数的平方根, 牛顿迭代法 - 梯度下降法
        :param x:
        :return:
        """
        # 保存目标数

        # 边界值
        if x < 0: raise Exception('can not be less than 0')
        if x == 0: return 0

        # 从x开始迭代
        self._a = x
        return self.my_sprt(x)

    def my_sprt(self, x):
        """
        一个数除以其平方根 再加上其平方根 的和除以2 就等于其平方根
        开平方公式:
        如果 y = sprt(x)
        则有 x[n+1] = x[n] + (y / x[n] - x[n]) / 2
        或者 x[n+1] = (x[n] + y / x[n]) / 2
        :param x:
        :return:
        """
        # 求 x 和 目标数/x 的平均数
        # 如果平均数不等于 x 则继续 用平均数 迭代
        ans = (x + self._a / x) / 2
        if ans == x:
            return x
        else:
            return self.my_sprt(ans)

    def mySprt2(self, x):
        """
        递归梯度下降法

        :param x:   要开平方的目标数
        :param rx:  迭代区间
        :param e:   精度
        :return:
        """


s1 = 4
s2 = 9
s3 = 8
s4 = 0
s5 = 10
s = [s1, s2, s3, s4, s5]

for p in s:
    print(p, '->', Solution().mySprt(p))
