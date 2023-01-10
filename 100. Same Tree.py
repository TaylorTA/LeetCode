# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def h(n1, n2):
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                else:
                    return h(n1.left, n2.left) and h(n1.right, n2.right)
            elif (n1 and not n2) or (n2 and not n1):
                return False
            else:
                return True
        return h(p,q)
