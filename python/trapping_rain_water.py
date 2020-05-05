from typing import List
from python.common.util import printCost


class Solution:

    @printCost
    def trap(self, height: List[int]) -> int:
        pass


s1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = [s1]

for p in s:
    print(p, '->', Solution().trap(p))
