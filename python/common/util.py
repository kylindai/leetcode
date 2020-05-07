import timeit


def printCost(fn):
    """
    打印耗时
    :param fn:
    :return:
    """
    def cost(*args):
        start = timeit.default_timer()
        ret = fn(*args)
        print('cost time: %.10f ms' % ((timeit.default_timer() - start) / 1000))
        return ret

    return cost


def printList(l, name=None, with_tail=True):
    """
    打印链表
    :param l:
    :param name:
    :param with_tail:
    :return:
    """
    if name:
        print(name, end=": ")
    while l:
        print(l.val, end='')
        l = l.next
        if l:
            print(' -> ', end='')
        else:
            if with_tail:
                print(' -> ', end='None')
            print('')
