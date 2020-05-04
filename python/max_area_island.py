import collections
from typing import List
from python.common.util import printCost


class Solution:

    @printCost
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        广度优先遍历基于队列
        :param grid:
        :return:
        """
        ans = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                cur = 0
                q = collections.deque([(i, j)])
                while q:
                    cur_i, cur_j = q.popleft()
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    grid[cur_i][cur_j] = 0
                    cur += 1
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ni, nj = cur_i + di, cur_j + dj
                        q.append((ni, nj))
                ans = max(cur, ans)
        return ans

    @printCost
    def maxAreaOfIsland3(self, grid: List[List[int]]) -> int:
        """
        深度优先遍历基于栈
        :param grid:
        :return:
        """
        ans = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                # 每一个点进行一次深度遍历
                cur = 0
                # 构建一个栈，待处理的点入栈
                stack = [(i, j)]
                while stack:
                    # 取栈顶的点
                    cur_i, cur_j = stack.pop()
                    # 如果点不满足要求，继续出栈
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    # 当前的点满足要求，改版点的状态
                    grid[cur_i][cur_j] = 0
                    # 累积处理的次数
                    cur += 1
                    # 当前点做4个方向的变更，然后入栈
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ni, nj = cur_i + di, cur_j + dj
                        stack.append((ni, nj))
                ans = max(cur, ans)
        return ans

    @printCost
    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                ans = max(self.dfs(grid, i, j), ans)
        return ans

    def dfs(self, grid, i, j) -> int:
        """
        深度遍历
        :param grid:
        :param i:
        :param j:
        :return:
        """
        # 递归的出口
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 1:
            return 0
        # 核心算法，走过的设为0
        grid[i][j] = 0
        # 累积数量
        ans = 1
        # 延4个方向改变坐标
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            ans += self.dfs(grid, ni, nj)
        # 返回
        return ans


s1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
      [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
s2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
s = [s1, s2]

for p in s:
    print('->', Solution().maxAreaOfIsland(p))
