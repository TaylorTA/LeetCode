from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.op = defaultdict(list)
    
    def helper(self, node, level):
        if node:
            self.op[level].append(node.val)
            self.helper(node.left, level+1)
            self.helper(node.right, level+1)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.helper(root,0)
        return [self.op[key] for key in sorted(self.op)]
