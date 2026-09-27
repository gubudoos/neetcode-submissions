# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow and fast pointers
        #    [1, 2, 3, 4]
        # s:  1, 2
        # f:  2, 4
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # list broken up into 2
        # need to reverse 2nd list
        # 3, 4 -> 4, 3

        l2 = slow.next
        # prev pointer of 2nd list is None: None -> 3 -> 4 -> None
        prev = None 
        # next pointer of 1st list is None: 1, 2 -> None
        slow.next = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        
        # l2 currently on None, so need to start from prev
        # l1: 1, 2, None
        # l2: 4, 3, None
        l1, l2 = head, prev
        while l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2




            

            

        