# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    
    def traversal (self, node, frequency):
        if node:
            frequency[node.val] += 1
            
            if not node.left and not node.right:
                odd = 0
                for i in range(len(frequency)):
                    if frequency[i]%2 == 1:
                        odd +=1
                if odd <= 1:
                    self.count += 1
                
            self.traversal(node.left, frequency)
            self.traversal(node.right, frequency)
            frequency[node.val] -= 1
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0
        frequency = [0 for _ in range(10)]
        self.traversal(root, frequency)
        return self.count
