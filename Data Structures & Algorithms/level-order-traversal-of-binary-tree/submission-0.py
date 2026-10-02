# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [[root,1]]
        res = []

        while stack:
            node, level = stack.pop()
            if not node:
                return res
            
            if len(res) < level:
                res.append([])
            res[level-1].append(node.val)
            
            if node.right:
                stack.append([node.right,level+1])
            if node.left:
                stack.append([node.left,level+1])
        return res

            

            

            

        