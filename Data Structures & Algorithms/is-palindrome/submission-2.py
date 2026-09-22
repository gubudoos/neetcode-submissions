import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = re.sub(r'[^A-Za-z0-9]', '', s.lower())
        new_s = new_s.replace(' ', '')
        # new_s = new_s.replace('?', '')
        # print(new_s)
        
        for i in range(0, len(new_s) // 2):
            if new_s[i] == new_s[-i-1]:
                continue
            else:
                return False
        return True