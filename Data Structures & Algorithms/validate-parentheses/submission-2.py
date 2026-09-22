class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        keymap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        # print(keymap.keys())

        for char in s:
            # print('char: ', char)
            if char not in keymap.keys():
                stack.append(char)
            elif stack and stack[-1] == keymap[char]:
                stack.pop()
            else:
                return False
        # print('stack: ', stack)
        return True if not stack else False

