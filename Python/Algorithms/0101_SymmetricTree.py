# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def symmetricSubtrees(self, r1: TreeNode, r2: TreeNode) -> bool:
        if not (r1 or r2):
            return True
        
        if r1 and r2 and r1.val == r2.val:
            return self.symmetricSubtrees(r1.left, r2.right) and self.symmetricSubtrees(r1.right, r2.left)

        return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.symmetricSubtrees(root.left, root.right)