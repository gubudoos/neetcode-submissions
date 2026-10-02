# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            qLen = len(q)
            num = None

            for i in range(qLen):
                node = q.popleft()
                if node and num == None:
                    num = node.val
                    q.append(node.right)
                    q.append(node.left)
                elif node and num != None:
                    q.append(node.right)
                    q.append(node.left)
                
            if num:
                res.append(num)
        return res
                

                






            
            


        