# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive approach
class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def recurse(root: TreeNode):
            if root:
                recurse(root.left)
                res.append(root.val)
                recurse(root.right)
            
        res = []
        recurse(root)
        return res


# Iterative approach
class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
            
        return res