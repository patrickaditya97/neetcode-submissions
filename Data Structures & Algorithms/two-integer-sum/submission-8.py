class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_hash = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in result_hash:
                result_hash[diff] = i
            else:
                return [result_hash[nums[i]], i]

        return [-1, -1]

            