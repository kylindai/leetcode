from typing import List
from python.common.util import printCost


class Solution:

    @printCost
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        l = len(nums)

        # 边界检查
        if not nums or l < 3:
            return ans

        # 排序
        nums.sort()

        # 第一个数处理
        for i in range(l - 2):

            # 大于0的数则结束
            a = nums[i]
            if a > 0:
                return ans

            # 去掉重复的数
            if i > 0 and a == nums[i - 1]:
                continue

            # 双指针
            L = i + 1
            R = l - 1
            while L < R:
                # 当三数之和为0
                b = nums[L]
                c = nums[R]
                if a + b + c == 0:
                    ans.append([a, b, c])
                    # 重复数处理
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif a + b + c > 0:
                    R -= 1
                else:
                    L += 1

        return ans

    @printCost
    def threeSum2(self, nums: List[int]) -> List[List[int]]:

        ans = []
        l = len(nums)

        # 边界处理
        if not nums or l < 3:
            return ans

        # 排序
        nums.sort()
        print(nums)

        # 去重
        # d = {}
        for i in range(l - 2):
            if nums[i] > 0:
                return ans
            # if nums[i] in d:
            #     continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    a = nums[i]
                    b = nums[j]
                    c = nums[k]
                    if (a + b + c) == 0:
                        ans.append([a, b, c])
                        # d[a] = [b, c]

        return ans


s1 = [-1, 0, 1, 2, -1, -4]
s = [s1]

for p in s:
    print(p, '->', Solution().threeSum(p))
