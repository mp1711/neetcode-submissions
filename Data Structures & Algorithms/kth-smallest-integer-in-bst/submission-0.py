# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(root, c):
            if not root or c==k: 
                return 

            inorder(root.left, c)

            res.append(root.val)
            print(res)
            c+=1
            if c==k:
                return

            inorder(root.right, c)
        
        inorder(root, 0)
        return res[k-1]
            

        