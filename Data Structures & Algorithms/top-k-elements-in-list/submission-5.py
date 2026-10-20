class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq_arr = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counter[num] = 1+counter.get(num, 0)

        for num, count in counter.items():
            freq_arr[count].append(num)

        result_arr = []
        for i in range(len(nums), -1, -1):
            if len(freq_arr[i]) != 0:
                for freq in freq_arr[i]:
                    result_arr.append(freq)
            
            if len(result_arr) == k:
                return result_arr

        return result_arr
