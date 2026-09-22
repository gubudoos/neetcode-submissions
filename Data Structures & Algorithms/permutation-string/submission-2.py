class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}

        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1
        # print(True if 'a' in s1_dict.keys() else False)
        
        len_s1 = len(s1_dict)

        for i in range(len(s2)):
            s2_dict = {}
            len_substr = 0
            for j in range(i, len(s2)):
                s2_dict[s2[j]] = s2_dict.get(s2[j], 0) + 1
                if s1_dict.get(s2[j], 0) < s2_dict[s2[j]]:
                    break
                if s1_dict.get(s2[j], 0) == s2_dict[s2[j]]:
                    len_substr += 1
                if len_substr == len_s1:
                    return True
                
        return False

