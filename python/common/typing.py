class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self._node = self

    def __str__(self):
        head = self
        info = []
        while head:
            info.append(str(head.val))
            head = head.next
        return ' -> '.join(info)

    def __iter__(self):
        return self

    def __next__(self):
        if not self._node:
            raise StopIteration
        else:
            node = self._node
            self._node = self._node.next
            return node
