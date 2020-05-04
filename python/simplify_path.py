from python.common.util import printCost


class Solution:

    @printCost
    def simplifyPath(self, path: str) -> str:
        # 按'/'分割path
        names = path.split('/')
        # print(names)
        stack = []
        for name in names:
            if name == '..':
                # 出栈
                if stack:
                    stack.pop()
            elif name and name != '.':
                # 入栈
                stack.append(name)
        # print(stack)
        # 生产 canonical path
        return '/' + '/'.join(stack)


s1 = '/home/'
s2 = '/home//foo/'
s3 = '/a/./b/../../c/'
s4 = '/a/../../b/../c//.//'
# s4 = ''
s5 = '///a//b////c/d//././/..'

s = [s1, s2, s3, s4, s5]
# s = [s4]
for p in s:
    print(p, '->', Solution().simplifyPath(p))
