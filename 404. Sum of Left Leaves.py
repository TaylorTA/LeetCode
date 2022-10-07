# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
        
    
    def helper(self, node, left):
        if node:
            if not node.left and not node.right and left:
                self.sum += node.val
            else:
                self.helper(node.left, True)
                self.helper(node.right, False)
    
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.helper(root, False)
        return self.sum
