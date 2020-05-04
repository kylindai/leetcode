from typing import List
from common.util import printCost


class Solution:

    @printCost
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, ans = 0, 0, 0
        d = {}
        # j是右边界
        # 遍历字符串
        for j, c in enumerate(s):
            # 如果c在集合里
            if c in d:
                # 计算左界
                # 左边界取这个字符在集合中的下标
                i = max(d[c], i)
            # 右界即遍历时的下标
            # 取右界-左届+1
            ans = max(ans, j - i + 1)
            # 当前字符及下标放入集合
            d[c] = j + 1
        return ans

    @printCost
    def lengthOfLongestSubstring2(self, s: str) -> int:
        ans = 1 if s else 0
        i, j, n = 0, 0, len(s)
        d = []
        while i < n and j < n:
            if s[j] not in d:
                # 如果字符不在集合里，则加入集合，滑动窗口右边界向右移动
                d.append(s[j])
                j += 1
                ans = max(ans, j - i)
                print(d)
            else:
                # 如果字符在集合中，则从集合中移除，滑动窗口左边界向右移动
                d.remove(s[i])
                i += 1
                print(d)
        return ans

    @printCost
    def lengthOfLongestSubstring3(self, s: str) -> int:
        """

        :param s:
        :return:
        """
        ans = 1 if s else 0
        # 遍历字符串
        for i, e in enumerate(s):
            # 从第2个字符开始，到第j个来判断该子串是否是不重复的
            for j in range(i + 1, len(s) + 1):
                # 如果子串不重复，则保存子串长度
                r = self.allUnique(s, i, j)
                if r:
                    ans = max(ans, j - i)
                print('[{}] {} unique'.format(s[i:j], "is" if r else "is not"))
        return ans

    def allUnique(self, s: str, start: int, end: int) -> bool:
        """
        判断字符串里的字符是否唯一
        :param s:
        :param start:
        :param end:
        :return:
        """
        a = set()
        for i in range(start, end):
            if s[i] in a:
                return False
            else:
                a.add(s[i])
        # print('allUnique s = ', s[start:end])
        return True


s = 'pwwkew'
s1 = ''
# print(max(3, 5))
# print(Solution().lengthOfLongestSubstring("abcabcbb"))
# print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring(s1))
# print(Solution().lengthOfLongestSubstring2(s))
