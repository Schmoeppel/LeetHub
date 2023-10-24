# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        queue = [(root, 0)]  # Initialize a queue with the root node
        layers = {}

        while queue:
            current_node, level = queue.pop(0)  # Dequeue the front node

            if level in layers:
                layers[level].append(current_node.val)
            else:
                layers[level] = [current_node.val]

            if current_node.left:
                queue.append((current_node.left, level+1))
            if current_node.right:
                queue.append((current_node.right, level+1))

        result = []
        for level in layers:
            result.append(max(layers[level]))

        return result