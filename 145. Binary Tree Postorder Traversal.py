# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node, op):
        if not node:
            return
        self.preorder(node.left, op)
        self.preorder(node.right, op)
        op.append(node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        op = []

        self.preorder(root, op)

        return op
