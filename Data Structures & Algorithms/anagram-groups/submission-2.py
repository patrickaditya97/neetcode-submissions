class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for str_ in strs:
            sorted_str = "".join(sorted(str_))
            if sorted_str in hash_map:
                hash_map[sorted_str].append(str_)
            else:
                hash_map[sorted_str] = [str_]

        result = []
        for key, val in hash_map.items():
            result.append(val)

        return result