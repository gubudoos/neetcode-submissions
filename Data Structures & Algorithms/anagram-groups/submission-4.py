class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_map = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if not new_map:
                new_map[sorted_str] = [string]
            else:
                if sorted_str in new_map.keys():
                    new_map[sorted_str].append(string)
                else:
                    new_map[sorted_str] = [string]
        
        output = []
        for value in new_map.values():
            output.append(value)
        return output
