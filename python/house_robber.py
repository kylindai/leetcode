from typing import List
from python.common.util import printCost
from python.common.typing import ListNode


class Solution:

    @printCost
    def rob(self, nums: List[int]) -> int:
        """
        n 为房间的个数
        当 n = 0, 则解为 f[0] = 0
        当 n = 1, 则抢劫 f[1] = A1
        当 n = 2, 则抢劫 f[2] = max(A1, A2)
        当 n = 3, 分2种情况
            1. 抢劫第3个: f[3] = f[1] + A3
            2. 抢劫第2个: f[2] = max(A1, A2)
            3. 最优解: f[3] = max(f[3 - 2] + A3, f[2])
        推导出递推公式: f[k] = max(f[k - 2] + Ak, f[k - 1])
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        # if n == 2:
        #     return max(nums[0], nums[1])

        # 这里为什么要 n + 1
        # 我们只计算最多n个房间, 迭代时计算f[0]
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]

        k = n
        for k in range(2, n + 1):
            dp[k] = max(dp[k - 2] + nums[k - 1], dp[k - 1])

        return dp[k]


s1 = [1, 2, 3, 1]
s2 = [2, 7, 9, 8, 1]
s3 = [7, 5]
s4 = [6]

s = [s1, s2, s3, s4]

for p in s:
    print(p, '->', Solution().rob(p))
