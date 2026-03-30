# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def dfs(root, path): 
            if not root.left and not root.right: 
                self.res += path
            
            if root.left: 
                path = path*10 + root.left.val
                dfs(root.left, path)
                path = path//10
            
            if root.right: 
                path = path*10 + root.right.val
                dfs(root.right, path)
                path = path//10
            
        dfs(root, root.val)

        return self.res
        