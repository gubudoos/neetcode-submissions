class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        max_range = len(nums)
        for i, num in enumerate(nums):
            diff = target - num
            for j in range(i+1, max_range):
                if nums[j] == diff:
                    return [i, j]

        