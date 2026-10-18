class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_hash = {}

        for num in nums:
            if num in freq_hash:
                freq_hash[num] += 1
            else:
                freq_hash[num] = 1

        sorted_freq_hash = dict(sorted(freq_hash.items(), key=lambda item: item[1], reverse=True)[:k])

        return list(sorted_freq_hash.keys())