class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])
        row = 0

        for i in range(rows):
            if matrix[i][0] > target:
                row = i - 1
                break

        else:
            row = rows - 1

        for j in range(cols):
            if matrix[row][j] == target:
                return True

        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

print(Solution().searchMatrix(matrix, target))
