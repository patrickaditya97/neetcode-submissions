class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp_t, temp_i = stack.pop()
                result[temp_i] = i - temp_i

            stack.append((t, i))

        return result