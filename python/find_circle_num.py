from typing import List
from python.common.util import printCost


class Solution:

    @printCost
    def findCircleNum(self, M: List[List[int]]) -> int:
        pass


s1 = [[1, 1, 0],
      [1, 1, 0],
      [0, 0, 1]]
s = [s1]

for p in s:
    print('->', Solution().findCircleNum(p))
