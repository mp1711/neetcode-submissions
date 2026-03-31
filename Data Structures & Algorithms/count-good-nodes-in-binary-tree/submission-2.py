# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxval): 

            if not root: 
                return 0
            
            elif root.val>=maxval: 
                maxval = max(maxval, root.val)
                return 1 + dfs(root.left, maxval) + dfs(root.right, maxval)
            
            else: 
                return dfs(root.left, maxval) + dfs(root.right, maxval)
        
        return dfs(root, root.val)

        