class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sim_map = {}

        for str_ in strs:
            char_array = [0] * 26
            for s in str_:
                char_array[ord(s) - ord('a')] += 1

            if tuple(char_array) in sim_map:
                sim_map[tuple(char_array)].append(str_)
            else:
                sim_map[tuple(char_array)] = [str_]


        return list(sim_map.values())
