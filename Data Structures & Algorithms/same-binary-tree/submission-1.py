# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1, l2 = [], []
        stack1, stack2 = [p], [q]

        while stack1 or stack2:
            if stack1:
                nodep = stack1.pop()
            else:
                nodep = None
            
            if stack2:
                nodeq = stack2.pop()
            else:
                nodeq = None

            if not nodep:
                l1.append(None)
            if not nodeq:
                l2.append(None)

            if nodep:
                l1.append(nodep.val)
                # l1.append(nodep.left.val)
                stack1.append(nodep.left)
                # l1.append(nodep.right.val)
                stack1.append(nodep.right)

            if nodeq:
                l2.append(nodeq.val)
                # l2.append(nodeq.left.val)
                stack2.append(nodeq.left)
                # l2.append(nodeq.right.val)
                stack2.append(nodeq.right)
        return l1 == l2
        