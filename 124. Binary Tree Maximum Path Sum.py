# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.m = -math.inf
        def helper(node):
            if node:
                l = max(0, helper(node.left))
                r = max(0, helper(node.right))
                self.m = max(self.m, l + r + node.val)
                return max(l+node.val, r+node.val)
            return 0
        helper(root)
        return self.m
