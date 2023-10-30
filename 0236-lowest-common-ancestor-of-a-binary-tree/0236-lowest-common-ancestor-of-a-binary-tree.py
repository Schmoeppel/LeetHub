# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.LCA = None

        def dfs(root, p, q):
            if root is None:
                return 0
            
            if root.val == p.val or root.val == q.val:
                #print(f"found it: {root.val}")
                res = 1 + dfs(root.left, p, q) + dfs(root.right, p, q)
            else:
                res = dfs(root.left, p, q) + dfs(root.right, p, q)

            if res >= 2:
                #print(f"found LCA: {root.val}")
                self.LCA = root
                res -= 1
            return res

        dfs(root, p, q)
        return self.LCA