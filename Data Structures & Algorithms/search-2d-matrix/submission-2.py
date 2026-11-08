class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        count = 0

        while low <= high:
            mid = low + (high - low) // 2

            i = mid // cols
            j = mid % cols

            # print(matrix[i][j], (i, j), mid)
            # count += 1

            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                low = mid + 1
            else:
                high = mid - 1


            # if count == 25:
            #     break

        return False