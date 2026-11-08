class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        len_nums = len(nums)
        left = 0
        right = len_nums - 1

        while left <= right:
            nums_mid = left + right - left // 2
            if nums[nums_mid] < target:
                left = nums_mid + 1
            elif nums[nums_mid] > target:
                right = nums_mid - 1
            else:
                return nums_mid

        return -1