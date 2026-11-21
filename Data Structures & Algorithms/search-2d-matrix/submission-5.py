class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        limit = (rows * cols) - 1

        left, right = 0, limit
        while left <= right:
            mid = left + (right - left) // 2

            i = mid // cols
            j = mid % cols

            element = matrix[i][j]

            if element == target:
                return True

            if element < target:
                left = mid + 1
            else:
                right = mid - 1

        return False