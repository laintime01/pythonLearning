class Solution(object):
    def updateMatrix(selfself, mat):
        # 获取行、列值
        m = len(mat)
        n = len(mat[0])
        # 初始化存储数组
        que = []
        # 遍历矩阵，遇到0就添加到数组中
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    que.append((i, j))
                # 这里需要将1初始化为其他值，此处设为-1，目的是方便后续判断是否已遍历该点
                elif mat[i][j] == 1:
                    mat[i][j] = -1
        # 初始化距离，第一轮遍历的点到0的距离应当为1
        dis = 1
        # 当当前层不为空时，逐个遍历层内元素
        while que:
            curlen = len(que)
            for i in range(curlen):
                # 每次取左边第一个元素遍历四个方向
                md = que.pop(0)
                for r, c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    x = md[0] + r
                    y = md[1] + c
                    # 若当前点索引不越界且值为-1，说明当前这一轮遇到了未遍历过的点，遍历一遍
                    if 0 <= x < m and 0 <= y < n and mat[x][y] == -1:
                        # 将原来的值改为轮数，0距离该点需要多少轮遍历即表示0到该点的距离
                        mat[x][y] = dis
                        # 将遍历过的点加入数组中，作为下一层遍历的元素
                        que.append((x, y))
            # 每完成一轮遍历距离+1
            dis += 1
        # 返回数组
        return mat
