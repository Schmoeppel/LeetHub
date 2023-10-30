# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_zigzag = 0
        
        def dfs(root, direction, zigzag_cnt):
            self.max_zigzag = max(self.max_zigzag, zigzag_cnt)
            if root is None:
                return
            else:
                if direction == 0:
                    dfs(root.left, 0, 0)
                    dfs(root.right, 1, zigzag_cnt+1)
                else:
                    dfs(root.left, 0, zigzag_cnt+1)
                    dfs(root.right, 1, 0)
                return
        
        dfs(root.left, 0, 0)
        dfs(root.right, 1, 0)

        return self.max_zigzag

