class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        history = []
        for num in sorted_nums:
            if not history:
                history.append(num)
            else:
                if num == history[-1]:
                    return True
                else:
                    history.append(num)
        return False