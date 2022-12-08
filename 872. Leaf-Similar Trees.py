# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
         self.t1 = []


    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    self.t1.append(node.val)
                dfs(node.left)
                dfs(node.right)
            
        dfs(root1)
        dfs(root2)

        return self.t1[:len(self.t1)//2] == self.t1[len(self.t1)//2:]
