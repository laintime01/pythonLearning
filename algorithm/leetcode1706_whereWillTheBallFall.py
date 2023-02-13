class Solution(object):
    def findBall(self, grid):
        """
        :param grid:
        :return:
        """
        n = len(grid[0])  # 每行长度
        ans = [-1] * n

        for i in range(n):
            place = i  # 球最开始的位置
            for j in grid:
                go = j[place]  # 球该怎么走
                place += go  # 左右都是+ 左为-1+ -1 右为 1+ 1
                # place<0:碰到左边墙, place ==n,因为最右边是n-1，所以是碰到右边墙
                # 如果左右不一样，说明遇见了V形
                if place < 0 or place == n or j[place] != go:
                    break
            else:  # 成功到达底部
                ans[i] = place
        return ans


grid_test = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]

print(Solution().findBall(grid_test))
