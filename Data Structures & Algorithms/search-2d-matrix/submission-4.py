class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = low + (high - low) // 2

            i = mid // cols
            j = mid % cols

            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False