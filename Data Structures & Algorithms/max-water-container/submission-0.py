class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        max_area = float('-inf')

        while(i < j):
            l_height = heights[i]
            r_height = heights[j]

            height = min(l_height, r_height)
            width = abs(i-j)

            max_area = max(max_area, height * width)

            if l_height < r_height:
                i += 1
            else:
                j -= 1


        return max_area