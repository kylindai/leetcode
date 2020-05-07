from typing import List
from python.common.typing import ListNode
from python.common.util import printCost, printList


class Solution:

    @printCost
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = ListNode()

        node = ans

        return ans

    @printCost
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        for x in l1:
            print(x.val)
        pass


"""
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
s1 = [ListNode(1, ListNode(4, ListNode(5))),
      ListNode(1, ListNode(3, ListNode(4))),
      ListNode(2, ListNode(6))]
s = [s1]

# for p in s:
#     print(Solution().mergeKLists(p))

l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
print(Solution().mergeTwoLists(l1, l2))
