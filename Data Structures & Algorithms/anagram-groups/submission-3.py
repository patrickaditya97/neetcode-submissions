class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_result = defaultdict(list)

        for str_ in strs:
            count = [0] * 26

            for letter in str_:
                count[ord(letter) - ord("a")] += 1

            temp_result[tuple(count)].append(str_)

        result = []
        for _, res in temp_result.items():
            result.append(res)

        return result