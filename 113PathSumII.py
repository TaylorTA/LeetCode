# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = []
        
        
    def helper(self, node, targetSum, curList):
        if node:
            curList.append(node.val)
            targetSum -= node.val
            if not node.left and not node.right:
                if targetSum == 0:
                    self.output.append(list(curList))
            self.helper(node.left, targetSum, curList)
            self.helper(node.right, targetSum, curList)
            curList.pop()
            targetSum += node.val
        
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.helper(root, targetSum, [])
        return self.output
