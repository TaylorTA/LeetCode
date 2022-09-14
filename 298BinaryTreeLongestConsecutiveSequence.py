# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxPath = 1
        
    def preorder(self, node, currLength, curr):
        if node:
            if node.val == (curr + 1):
                currLength += 1
                if currLength > self.maxPath:
                    self.maxPath = currLength
            else:
                currLength = 1
            
            self.preorder(node.left, currLength, node.val)
            self.preorder(node.right, currLength, node.val)
        
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            self.preorder(root, 1, root.val)
            return self.maxPath
