# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leaf_sequence(root):
            if root == None:
                return []
            elif root.left or root.right:
                return [] + get_leaf_sequence(root.left) + get_leaf_sequence(root.right)
            else:
                return [root.val]

        sequence1 = get_leaf_sequence(root1)

        sequence2 = get_leaf_sequence(root2)

        return sequence1 == sequence2