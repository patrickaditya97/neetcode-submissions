class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        len_nums = len(nums) + 1
        freq_arr = [[] for i in range(len_nums)]
        freq_map = Counter(nums)
        
        for num, count in freq_map.items():
            freq_arr[count].append(num)

        result = []
        for i in range(len_nums-1, -1, -1):
            if len(freq_arr[i]) != 0:
                result = result + freq_arr[i]

        return result[:k]