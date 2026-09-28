class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] > 1:
                return num
        
        