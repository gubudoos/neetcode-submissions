class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = 0
        self.next = None

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow
        
        # hashmap = {}
        
        # for num in nums:
        #     hashmap[num] = hashmap.get(num, 0) + 1
        #     if hashmap[num] > 1:
        #         return num
        
        # dummy = ListNode()
        # l1 = dummy
        # l2 = dummy
        # l, r = 0, len(nums)-1

        # while l < r:



        
        