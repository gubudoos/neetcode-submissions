class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [[], [1], [2], [8]]
        # suffix = [[48], [24], [6], []]

        prefix, suffix = [], []

        last_prefix = 1
        last_suffix = 1
        for i, num in enumerate(nums):
            if not prefix:
                prefix.append(last_prefix)
            if not suffix:
                suffix.append(last_suffix)
            else:
                last_prefix *= nums[i-1]
                prefix.append(last_prefix)

                last_suffix *= nums[-i]
                suffix.append(last_suffix)
        # print(prefix)
        # print(suffix)
        output = []
        for i, num in enumerate(prefix):
            output.append(prefix[i] * suffix[-i-1])
        return output
