from typing import List
from python.common.util import printCost, printList
from python.common.typing import ListNode


class Solution:

    @printCost
    def maxProfit(self, prices: List[int]) -> int:
        pass


s1 = [7, 1, 5, 3, 6, 4]
s = [s1]

for p in s:
    print(s1, '->', Solution().maxProfit(p))
