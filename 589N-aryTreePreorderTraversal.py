"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.po = []
        
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            self.po.append(root.val)
            if root.children:
                for child in root.children:
                    self.preorder(child)
        return self.po
