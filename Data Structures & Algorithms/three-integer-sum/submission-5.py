class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_set = sorted(nums)
        result = set()

        for i in range(len(nums_set) - 2):
            l = i + 1
            r = len(nums_set) - 1
            
            while l < r:
                if nums_set[l] + nums_set[r] + nums_set[i] == 0:
                    result.add((nums_set[l], nums_set[r], nums_set[i]))
                    l += 1
                    r -= 1
                elif nums_set[l] + nums_set[r] + nums_set[i] > 0:
                    r -= 1
                elif nums_set[l] + nums_set[r] + nums_set[i] < 0:
                    l += 1

        return list(result)

