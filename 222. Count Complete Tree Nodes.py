# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.n = 0

    def helper(self, cur):
        if cur:
            self.n += 1
            self.helper(cur.left)
            self.helper(cur.right)
    

    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.n
