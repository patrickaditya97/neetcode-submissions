class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_hash = defaultdict(list)

        result = []
        for str_ in strs:
            arr_freq = [0] * 26
            for i in range(len(str_)):
                arr_freq[ord(str_[i]) - ord('a')] += 1

            freq_hash[tuple(arr_freq)].append(str_)


        return list(freq_hash.values())