from typing import List
from python.common.util import printCost


class Solution:

    @printCost
    def maxProfit(self, prices: List[int]) -> int:
        """
        动态规划解法
        :param prices:
        :return:
        """
        # 递归方程
        # 初始边界

        ans = 0

        return 0


s1 = [7, 1, 5, 3, 6, 4]
s = [s1]

for p in s:
    print(s1, '->', Solution().maxProfit(p))
