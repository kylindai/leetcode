class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        return self

    def __next__(self):
        """
        some wrong with this function
        :return:
        """
        n = self.next
        if n:
            return n
        else:
            raise StopIteration
