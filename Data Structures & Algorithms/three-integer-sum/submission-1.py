class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_set = sorted(nums)
  
        print(num_set)
        result = set()
        for i in range(0, len(num_set)-2):
            l = i + 1
            r = len(num_set) - 1

            while l < r:
                if num_set[l] + num_set[r] == -1 * num_set[i]:
                    result.add((num_set[l], num_set[r], num_set[i]))
                    l += 1
                    r -= 1
                elif num_set[l] + num_set[r] + num_set[i] > 0:
                    r -= 1
                elif num_set[l] + num_set[r] + num_set[i] < 0:
                    l += 1
                


        return list(result)