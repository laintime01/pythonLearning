# leetcode 695


class Solution(object):
    def maxAreaOfIsland(self, grid):
        ans = 0
        for x, l in enumerate(grid):
            for y, j in enumerate(l):
                cur = 0
                stack = [(x, y)]
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                while stack:
                    cur_x, cur_y = stack.pop()
                    if cur_x < 0 or cur_y < 0 or cur_x == len(grid) or cur_y == len(grid[0]) or grid[cur_x][cur_y] != 1:
                        continue
                    cur += 1
                    grid[cur_x][cur_y] = 0
                    for dx, dy in directions:
                        next_x, next_y = cur_x + dx, cur_y + dy
                        stack.append((next_x, next_y))
                ans = max(ans, cur)
        return ans


# test
grid_example = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
except_result = 6
solution = Solution()
if solution.maxAreaOfIsland(grid_example) == except_result:
    print("test passed!")
