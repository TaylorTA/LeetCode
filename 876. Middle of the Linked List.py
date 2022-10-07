# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
        
        
    def helper(self, node, curr):
        if node:
            if not node.left and not node.right:
                self.max = max(self.max, curr)
            else:
                self.helper(node.left, curr+1)
                self.helper(node.right, curr+1)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 1)
        return self.max
