class Solution:
    def findMin(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if nums[0] < nums[len_nums - 1]:
            return nums[0]
        elif len_nums == 2:
            return min(nums)
        elif len_nums == 1:
            return nums[0]
        elif len_nums == 0:
            return -1

        
        left = 0
        right = len_nums - 1
        result = float('inf')
        mid = left + (right - left) // 2
        while left < right:
            mid = left + (right - left) // 2
            result = min(result, nums[left], nums[mid], nums[right])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1


        return result