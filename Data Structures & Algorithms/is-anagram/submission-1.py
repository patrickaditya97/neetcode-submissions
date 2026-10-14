class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        len_s = len(s)

        s_freq = {}
        t_freq = {}
        for i in range(len_s):
            if s[i] not in s_freq:
                s_freq[s[i]] = 1
            else:
                s_freq[s[i]] += 1

            if t[i] not in t_freq:
                t_freq[t[i]] = 1
            else:
                t_freq[t[i]] += 1

        for (s_key, s_val) in s_freq.items():
            if s_key in t_freq:
                if t_freq[s_key] != s_val:
                    return False
            else:
                return False
            
        

        return True