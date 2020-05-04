from typing import List
from python.common.util import printCost


class Solution:

    @printCost
    def restoreIpAddresses(self, s: str) -> List[str]:

        d = {}
        ans = set()

        def dfs(s: str, res=[]):
            """

            :param s: 子串
            :param res: 传递最后结果
            :return:
            """
            print('dfs(\'{}\', {})'.format(s, res))

            # 边界检查
            if len(s) > 12:
                return

            # 递归出口1, 串未遍历完, 已拆分了4组
            if s and len(res) == 4:
                print('dfs-over-1 s not empty, but res == 4')
                return

            # 递归出口2, 串遍历完, 已拆分小于4组
            if not s and len(res) < 4:
                print('dfs-over-2 s is empty, but res < 4')
                return

            # 递归终止，串遍历完，已拆分了4组
            if not s and len(res) == 4:
                item = '.'.join(res)
                # if item not in d:
                ans.add(item)
                # d[item] = 1
                print('dfs-over')
                return

            for i in range(1, 4):
                ip = s[:i]
                # if len(res) == 3:
                #     continue
                if not ip:
                    print('dfs-over-2 ip is empty')
                    return
                if len(ip) > 1 and ip[0] == '0':
                    print('dfs-over-3 ip is start with 0', s, ip)
                    return
                if int(ip) <= 255:
                    dfs(s[i:], res + [ip])

        dfs(s)
        return ans

    @printCost
    def restoreIpAddresses2(self, s: str) -> List:
        l = len(s)
        ips = []
        for i in range(1, 4):
            ip1 = s[0:i]
            if self.invalid(ip1):
                continue;
            for j in range(i + 1, i + 4):
                ip2 = s[i:j]
                if self.invalid(ip2):
                    continue;
                for k in range(j + 1, l):
                    ip3 = s[j:k]
                    if self.invalid(ip3):
                        continue;
                    ip4 = s[k:]
                    if self.invalid(ip4):
                        continue;
                    # print("%s.%s.%s.%s" % (ip1, ip2, ip3, ip4))
                    if int(ip1) <= 255 and int(ip2) <= 255 and int(ip3) <= 255 and int(ip4) <= 255:
                        ips.append("%s.%s.%s.%s" % (ip1, ip2, ip3, ip4))
        return ips

    def invalid(self, ip: str) -> bool:
        return len(ip) > 1 and ip[0] == '0'


s1 = '25525511135'
s2 = '19216800'
s3 = '1111'
s4 = '101023'
s = [s1, s2, s3, s4]
s = [s4]
for p in s:
    print(p, '->', Solution().restoreIpAddresses(p))

# a = [1,2]
# b = [3,4]
# print(a+b)

print('123'[:8])
