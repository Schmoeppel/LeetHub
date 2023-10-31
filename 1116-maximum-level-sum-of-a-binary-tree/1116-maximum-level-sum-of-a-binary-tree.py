# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        sums = [float("-inf")]
        while queue:
            cur, level = queue.popleft()
            if len(sums) <= level:
                sums.append(0)
            sums[level] += cur.val
            if cur.left:
                queue.append((cur.left, level+1)) 
            if cur.right:    
                queue.append((cur.right, level+1)) 

        return sums.index(max(sums))