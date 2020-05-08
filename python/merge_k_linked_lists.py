from typing import List
from python.common.typing import ListNode
from python.common.util import printCost

import heapq


class Solution:

    @printCost
    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
        """
        用堆排序（优先队列）选择最小的元素，生成结果链表
        :param lists:
        :return:
        """
        # 边界处理
        if not lists or len(lists) == 0:
            return None

        heap = []
        for l in lists:
            while l:
                # 构建小顶堆
                heapq.heappush(heap, l.val)
                l = l.next

        ans = ListNode()
        node = ans

        while heap:
            # 从堆中弹出最小元素，构建链表节点
            node.next = ListNode(heapq.heappop(heap))
            # 链表向前走
            node = node.next

        return ans.next

    @printCost
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        """
        依次两两合并法
        :param lists:
        :return:
        """
        ans = ListNode()

        for l in lists:
            ans = self.mergeTwoLists(ans, l)

        return ans.next

    @printCost
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        分治法两两合并
        :param lists:
        :return:
        """
        # 边界情况
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

        # 寻找中值
        mid = len(lists) // 2

        # 递归调用 mergeKLists
        return self.mergeTwoLists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))

    @printCost
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        合并2个有序链表
        :param l1:
        :param l2:
        :return:
        """
        # 边界处理
        if not l1 or not l2:
            return l1 if l1 else l2

        ans = ListNode()
        node = ans

        a, b = l1, l2
        while a and b:
            if a.val < b.val:
                node.next = a
                a = a.next
            else:
                node.next = b
                b = b.next
            node = node.next

        node.next = a if a else b

        return ans.next


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

for p in s:
    print(Solution().mergeKLists(p))

# l1 = ListNode(1, ListNode(4, ListNode(5)))
# l2 = ListNode(1, ListNode(3, ListNode(4)))
# print(Solution().mergeTwoLists(l1, l2))
