class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        i = 0
        c_s1 = Counter(s1)
        for j in range(len(s2)):
            if j - i + 1 > len(s1):
                i += 1

            c_s2 = Counter(s2[i: j + 1])

            if c_s1 == c_s2:
                return True


        return False