from typing import List
from python.common.util import printCost
from python.common.typing import ListNode


class Solution:

    def __init__(self):
        self._step = 1

    @printCost
    def climbStairs(self, n: int) -> int:
        """
        动态规划算法
        递推公式：climb[i] = climb[i - 1] + climb[i - 2]
        :param n:
        :return:
        """
        climb = {0: 0, 1: 1, 2: 2}
        i = n
        for i in range(3, n + 1):
            climb[i] = climb[i - 1] + climb[i - 2]
        return climb[i]

    @printCost
    def climbStairs3(self, n: int) -> int:
        """
        暴力解法+缓存
        :param n:
        :return:
        """
        memo = [0] * (n + 1)
        return self.climb_stairs2(0, n, memo)

    @printCost
    def climbStairs2(self, n: int) -> int:
        """
        暴力解法
        :param n:
        :return:
        """
        return self.climb_stairs(0, n)

    def climb_stairs(self, i, n):
        """
        递归函数
        :param i:
        :param n:
        :return:
        """
        print('step:', self._step, '-> climb_stairs: i=', i, "n=", n)
        self._step += 1
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_stairs(i + 1, n) + self.climb_stairs(i + 2, n)

    def climb_stairs2(self, i, n, memo):
        """
        带缓存的递归函数
        :param i:
        :param n:
        :param memo:
        :return:
        """
        print('step:', self._step, '-> climb_stairs2: i=', i, "n=", n)
        self._step += 1
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb_stairs2(i + 1, n, memo) + self.climb_stairs2(i + 2, n, memo)
        return memo[i]


s1 = 5
s2 = 3
s = [s1]

for p in s:
    print(p, '->', Solution().climbStairs(p))
