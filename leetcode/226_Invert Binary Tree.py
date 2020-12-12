# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# solution2
# from collections import deque
#
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         Q = deque([root])
#
#         while Q:
#             node = Q.popleft()
#
#             if node:
#                 node.left, node.right = node.right, node.left
#                 Q += [node.left]
#                 Q += [node.right]
#
#         return root

# solution3 - stack with 전위순회
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         stack = [root]
#
#         while stack:
#             node = stack.pop()
#
#             if node:
#                 node.left, node.right = node.right, node.left
#                 stack += [node.left]
#                 stack += [node.right]
#
#         return root