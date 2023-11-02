# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.true_avg_cnt = 0

        def dfs(root):
            if not root:
                return [0, 0]
            left_sum, left_cnt = dfs(root.left)
            right_sum, right_cnt = dfs(root.right)
            cur_sum =  left_sum + right_sum + root.val
            node_cnt = 1 + left_cnt + right_cnt
            cur_avg = cur_sum // node_cnt
            if cur_avg == root.val:
                self.true_avg_cnt += 1
            return [cur_sum, node_cnt]
    
        dfs(root)

        return self.true_avg_cnt