class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []
        
        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                temp_t, temp_ind = stack.pop()
                result[temp_ind] = ind - temp_ind

            stack.append((temp, ind))

        return result