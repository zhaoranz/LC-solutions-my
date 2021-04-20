"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res =[root.val]
        for c in root.children:
            if c : 
                res += self.preorder(c)
                
        return res

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack =[root]
        res =[]
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])
        return res
        
