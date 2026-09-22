class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_list = []
        # t_list = []
        # for l1, l2 in zip(s,t):
        #     s_list.append(l1)
        #     t_list.append(l2)
        # return True if sorted(s_list) == sorted(t_list) else False

        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))
        return True if s_sorted == t_sorted else False
        