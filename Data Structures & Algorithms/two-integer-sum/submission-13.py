class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        # Key = difference, value = index
        # storing difference allows you to store an anticipated value
        # You can also use 2 pointers
        for i in range(len(nums)):
            diff = target - nums[i]
            # print(diff, nums[i], visited)
            if nums[i] in visited:
                return [visited[nums[i]], i]
            else:
                visited[diff] = i

        return [-1, -1]