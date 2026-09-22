class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorted_nums = sorted(nums)
        # res = 0
        # highest_res = 0
        # last_num = 0
        # # print(sorted_nums)

        # for num in sorted_nums:
        #     # print('res: ', res)
        #     # print('last_num: ', last_num)
        #     # print('num: ', num)
        #     if res == 0:
        #         last_num = num
        #         res += 1
        #     else:
        #         if num - last_num == 1:
        #             last_num = num
        #             res += 1
        #         elif num - last_num == 0:
        #             continue
        #         else:
        #             highest_res = res if res >= highest_res else 0
        #             res = 0
        
        # highest_res = res if res >= highest_res else highest_res
        # return highest_res

        nums_set = set(nums)
        res = 0

        for nums in nums_set:
            if (nums-1) not in nums_set:
                length = 1
                while (nums+length) in nums_set:
                    length += 1
                res = max(res, length)
        return res
            
            
        