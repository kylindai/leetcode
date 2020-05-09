from python.common.util import printCost
import math


class Solution:

    @printCost
    def myCurt(self, x: int) -> int:
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
        return self.my_curt(x)

    def my_curt(self, x):
        """
        开立方公式:
        如果: y = curt(x)
        则有: x[n+1] = x[n] + (y / (x[n] * x[n]) - x[n]) / 3
        或者: x[n+1] = (2 * x[n] + y / x[n] / x[n]) / 3
        :param x:
        :return:
        """
        ans = (2 * x + self._a / x / x) / 3
        if ans == x:
            return x
        else:
            return self.my_curt(ans)


s1 = 8
s2 = 27
s = [s1, s2]

for p in s:
    print(p, '->', Solution().myCurt(p))
