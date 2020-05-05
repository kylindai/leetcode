from typing import List
from python.common.util import printCost
from python.common.typing import ListNode


class Solution:

    @printCost
    def reverseList(self, head: ListNode) -> ListNode:
        """
        将当前节点的 next 指针改为指向前一个元素
        双指针迭代
        :param head:
        :return:
        """
        # 当前指针
        c = head
        # 目标指针
        p = None
        while c:
            self.printList('c', c)
            self.printList('p', p)

            # 下一个节点暂存一下
            n = c.next

            # 修改当前节点的下一个节点，指向目标节点
            c.next = p

            # 当前节点指向目标节点
            # 目标节前向前移动
            p = c

            # 当前节点指向下一个节点
            # 当前节点向后移动
            c = n

        self.printList('p', p)
        return p

    def printList(self, name, l):
        print(name, end=": ")
        while l:
            print(l.val, end='->')
            l = l.next
        print('NULL')


s1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print('->', Solution().reverseList(s1))
