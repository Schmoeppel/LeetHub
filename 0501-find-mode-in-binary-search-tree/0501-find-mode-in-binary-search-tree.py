# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        occurences = defaultdict(int)

        def dsf(root):
            if root is None:
                return
            occurences[root.val] += 1
            dsf(root.left)
            dsf(root.right)

        dsf(root)
        max_count = max(occurences.values())

        return [key for key, value in occurences.items() if value == max_count]