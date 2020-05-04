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
