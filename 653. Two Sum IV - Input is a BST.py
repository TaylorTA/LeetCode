# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic = defaultdict(int)
        
    
    def helper(self, node, k):
        if node:
            if k - node.val in self.dic:
                return True
            self.dic[node.val] = 1
            return self.helper(node.left, k) or self.helper(node.right, k)
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.helper(root,k)
