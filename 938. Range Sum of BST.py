# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.s = 0


    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node:
                #print(node)
                if low <= node.val and node.val <= high:
                    self.s += node.val
                    dfs(node.left)
                    dfs(node.right)
                elif low > node.val:
                    dfs(node.right)
                else:
                    dfs(node.left)

        dfs(root)
        return self.s
