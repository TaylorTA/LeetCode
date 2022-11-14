# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node, op):
        if not node:
            return
        self.inorder(node.left, op)
        op.append(node.val)
        self.inorder(node.right, op)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        op = []

        self.inorder(root, op)

        return op
