class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # new_map = defaultdict(list)
        # for string in strs:
        #     sorted_str = "".join(sorted(string))
        #     new_map[sorted_str].append(string)
        # return list(new_map.values())

        res = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(string)
        return list(res.values())
            
