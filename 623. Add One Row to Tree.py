# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, val, depth, curr):
        if node:
            curr += 1
            if curr == depth:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
            
            self.helper(node.left, val, depth, curr)
            self.helper(node.right, val, depth, curr)
    
    
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        
        self.helper(root, val, depth, 1)
        
        return root
