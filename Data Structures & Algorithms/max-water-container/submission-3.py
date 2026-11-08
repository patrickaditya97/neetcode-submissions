class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_area = 0
        while(left < right):
            left_h, right_h = heights[left], heights[right]
            max_area = max(max_area, (right - left) * min(left_h, right_h))

            if left_h > right_h:
                right -= 1
            elif right_h > left_h:
                left += 1
            else:
                right -= 1
                left += 1

        return max_area