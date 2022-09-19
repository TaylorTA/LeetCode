# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pval = -math.inf
    
    def helper(self, node):
        if node:
            if not self.helper(node.left):
                return False
            if node.val <= self.pval:
                return False
            self.pval = node.val
            if not self.helper(node.right):
                return False
        return True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)
