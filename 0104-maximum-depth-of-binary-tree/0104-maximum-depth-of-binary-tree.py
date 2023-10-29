# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [root]

        level = 1
        max_level = 0

        while stack:
            node = stack.pop(0)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            level -= 1

            if level == 0:
                max_level += 1
                level = len(stack)
            
        return max_level
            