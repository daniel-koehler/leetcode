# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive approach
class SolutionRecursion:
    
    def explore(self, root: TreeNode, depth: int) -> int:
        if not root:
            return depth
        return max(self.explore(root.left, depth+1), self.explore(root.right, depth+1))
    
    def maxDepth(self, root: TreeNode) -> int:
        return self.explore(root, 0)

# Iterative approach (BFS)
class SolutionIterative:
    
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        nodes = [root]
        depth = 0
        while nodes:
            depth += 1
            for i in range(len(nodes)):
                curr = nodes.pop(0)
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)

        return depth

# Iterative approach (BFS) using deque from collections
class SolutionIterativeDeque:
    
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        nodes = deque([root])
        depth = 0
        while nodes:
            depth += 1
            for i in range(len(nodes)):
                curr = nodes.popleft()
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)

        return depth