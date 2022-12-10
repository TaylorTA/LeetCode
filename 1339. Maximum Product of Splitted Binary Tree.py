# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.aSum = []

        def helper(root):
            cs = 0
            if root:
                ls = helper(root.left)
                rs = helper(root.right)
                cs = ls + rs + root.val
                self.aSum.append(cs)
            return cs

        ts = helper(root)
        mp = 0
        #print(self.aSum)
        for s in self.aSum:
            mp = max(mp, s * (ts-s))
        
        return mp % (10**9+7)
