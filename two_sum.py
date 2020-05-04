from typing import List
from common.util import printCost


class Solution:

    @printCost
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        # 遍历数组的每个元素
        for i, num in enumerate(nums):
            # 查差值是否在表里
            c = target - num
            if c in d:
                return [d[c], i]
            else:
                # 表里保存差值元素的index
                d[num] = i
        return []

    @printCost
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            c = target - nums[i]
            if c in d and c != nums[i]:
                return [i, d[c]]
        return []

    @printCost
    def twoSum2(self, nums, target):
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum1([2, 7, 11, 15], 9))
print(Solution().twoSum2([2, 7, 11, 15], 9))
# print(Solution().twoSum2([3, 2, 4], 6))
