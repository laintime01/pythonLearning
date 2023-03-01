class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        line = None
        if target < matrix[0][0]:
            return False
        elif target > matrix[m - 1][0]:
            line = m - 1
        else:
            left = 0
            right = m - 1
            while left <= right:
                if left >= right - 1:
                    if matrix[right][0] == target:
                        return True
                    elif matrix[right][0] < target:
                        line = right
                    else:
                        line = left
                    break
                mid = (left + right) / 2
                if matrix[mid][0] == target:
                    return True
                elif matrix[mid][0] > target:
                    right = mid - 1
                else:
                    left = mid

        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) / 2
            if matrix[line][mid] == target:
                return True
            elif matrix[line][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False