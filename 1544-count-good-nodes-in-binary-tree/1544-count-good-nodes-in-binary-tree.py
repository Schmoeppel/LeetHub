# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, max_val, good_nodes):
            if not root:
                return good_nodes

            if root.val >= max_val:
                good_nodes += 1
            
            if root.val > max_val:
                max_val = root.val
            
            return dfs(root.left, max_val, good_nodes) + dfs(root.right, max_val, 0)

        return dfs(root, root.val, 0)