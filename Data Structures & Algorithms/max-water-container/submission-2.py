class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1

        max_area = 0

        while i < j:
            l_h = heights[i]
            r_h = heights[j]

            max_area = max(max_area, (j - i) * min(l_h, r_h))
            if l_h < r_h:
                i += 1
            else:
                j -= 1
                
            


        return max_area