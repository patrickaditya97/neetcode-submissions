class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        visited = set()
        len_nums = len(nums)
        nums.sort()
        print(nums)


        for ind_f, first in enumerate(nums[:len_nums - 2]):
            ind_s = ind_f + 1
            ind_t = len_nums - 1

            while ind_s < ind_t:
                second = nums[ind_s]
                third = nums[ind_t]

                if first + second + third < 0:
                    ind_s += 1
                elif first + second + third > 0:
                    ind_t -= 1
                elif first + second + third == 0:
                    result_set.add((first, second, third))
                    visited.add(first)
                    visited.add(second)
                    visited.add(third)

                    ind_s += 1
                    ind_t -= 1


        return list(result_set)