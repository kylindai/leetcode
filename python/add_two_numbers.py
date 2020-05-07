from typing import List
from python.common.util import printCost, printList
from python.common.typing import ListNode

import math


class Solution:

    @printCost
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ans = ListNode()

        # 结果链表的首地址赋值给node
        node = ans

        p, q = l1, l2
        carry = 0

        while p or q:

            a = p.val if p else 0
            b = q.val if q else 0

            # 计算和(+进位)
            sum = a + b + carry

            # 计算进位
            carry = sum // 10

            # 和取余作为结果链表下一个节点的val
            node.next = ListNode(sum % 10)

            # 结果链表下一个节点的地址赋值给自己，链表向前移动
            node = node.next

            if p: p = p.next
            if q: q = q.next

        if carry > 0:
            node.next = ListNode(1)

        # 从第二个节点返回
        return ans.next


s1 = ListNode(2, ListNode(4, ListNode(3)))
s2 = ListNode(5, ListNode(6, ListNode(4)))

print(printList(s1, with_tail=False), '+', printList(s2, with_tail=False), '->',
      printList(Solution().addTwoNumbers(s1, s2), with_tail=False))
