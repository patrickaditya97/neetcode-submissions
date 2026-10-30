class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        i = 0
        max_len = 0

        result = 0

        for j in range(len(s)):
            freq_map[s[j]] = 1 + freq_map.get(s[j], 0)

            max_len = max(max_len, freq_map[s[j]])

            while (j - i + 1) - max_len > k:
                freq_map[s[i]] -= 1
                i += 1

            result = max(result, j - i + 1)

        return result