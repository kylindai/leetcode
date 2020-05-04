from typing import List
from python.common.util import printCost


class Solution:

    @printCost
    def search(self, nums: List[int], target: int) -> int:

        # 边界case
        if not nums: return -1
        if len(nums) == 1: return 0 if target == nums[0] else -1

        l, r, m = 0, len(nums) - 1, 0
        while l <= r:
            # 计算中间位置
            m = int(l + (r - l) / 2)
            # 返回满足条件的下标
            if target == nums[m]: return m

            # 左边是有序数组
            if nums[l] <= nums[m]:
                if nums[l] <= target and target < nums[m]:
                    # 如果target位于m左边，则调整右界
                    r = m - 1
                else:
                    # 如果target位于m右边，则调整左界
                    l = m + 1
            # 左边不是有序数组
            else:
                if nums[m] < target and target <= nums[r]:
                    # 如果target位于m右边, 则调整左界
                    l = m + 1
                else:
                    # 如果target位于m左边, 则调整右界
                    r = m - 1

        return -1

    @printCost
    def search2(self, nums: List[int], target: int) -> int:

        # 边界case
        if not nums: return -1
        if len(nums) == 1: return 0 if target == nums[0] else -1

        # 二分查找分界点
        p = self.findP(nums)
        if p < 0:
            # 单调递增
            p = self.findT(nums, 0, len(nums) - 1, target)
        elif nums[0] < target:
            # target位于左边
            p = self.findT(nums, 0, p, target)
        else:
            # target位于右边
            p = self.findT(nums, p + 1, len(nums) - 1, target)

        return p if target == nums[p] else -1

    def findP(self, nums: List[int]) -> int:
        """
        找到旋转后的分界点
        :param nums:
        :return:
        """
        l, r, m = 0, len(nums) - 1, 0
        if nums[l] < nums[r]: return -1
        """
        [4, 5, 6, 7, 0, 1, 2]
        """
        while l < r:
            m = int(l + (r - l + 1) / 2)
            if nums[m] < nums[0]:
                r = m - 1
            else:
                l = m
        return l

    def findT(self, nums: List[int], l: int, r: int, target: int) -> int:
        """
        找到target的下标
        :param nums:
        :param l:
        :param r:
        :param target:
        :return:
        """
        m = 0
        while l < r:
            m = int(l + (r - l) / 2)
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l


s1 = [4, 5, 6, 7, 0, 1, 2, 3]
s2 = [3, 4, 5, 6, 7, 8, 0, 1, 2]
s3 = [1, 3]
s = [s1, s2, s3]

for p in s:
    print(p, '->', Solution().search(p, 3))
    # print(p, '->', Solution().search(p, 3))
