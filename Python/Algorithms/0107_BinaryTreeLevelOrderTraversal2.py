# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        nodes = deque([root])
        level_order = []
        while nodes:
            level_order.insert(0, [])
            for i in range(len(nodes)):
                curr = nodes.popleft()
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)                
                level_order[0].append(curr.val)
        return level_order