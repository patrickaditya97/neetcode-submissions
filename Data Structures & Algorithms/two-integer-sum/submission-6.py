class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if nums[i] in diff_map:
                return [diff_map[nums[i]], i]

            diff_map[diff] = i

        return [-1, -1] 