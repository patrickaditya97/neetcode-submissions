class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        freq_map = {s[0]: 1}
        max_len = 0
        i = 0
        
        for j in range(1, len(s)):
            while s[j] in freq_map:
                freq_map.pop(s[i])
                i+=1

            freq_map[s[j]] = 1

            max_len = max(max_len, j - i + 1)

        return max_len