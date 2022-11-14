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
        op.append(node.val)
        self.preorder(node.left, op)
        self.preorder(node.right, op)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        op = []

        self.preorder(root, op)

        return op
