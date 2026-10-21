class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result_arr = [0, 0]

        i = 0
        j = len(numbers) - 1

        while(i < j):
            two_sum = numbers[i] + numbers[j]

            if two_sum < target:
                i += 1
            elif two_sum > target:
                j -= 1
            elif two_sum == target:
                result_arr[0] = i+1
                result_arr[1] = j+1

                return result_arr


        return result_arr