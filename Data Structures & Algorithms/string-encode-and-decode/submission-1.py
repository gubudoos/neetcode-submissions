class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        sizes = []
        all_strings = ''
        for string in strs:
            sizes.append(str(len(string)))
            all_strings += string

        pre_size = ','.join(sizes)+'#'+all_strings
        # print(pre_size)
        return pre_size



    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes_str = ''
        msg_str = ''
        for i, char in enumerate(s):
            if char != '#':
                sizes_str += char
            else:
                msg_str = s[i+1:]
                break
        sizes_list = [int(x) for x in sizes_str.split(',')]
        # print(sizes_list)
        # print(msg_str)
        res = []
        for size in sizes_list:
            res.append(msg_str[:size])
            msg_str = msg_str[size:]

        return res


