# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        maxdepth=0
        def bfs(maxdepth):
            Q = deque()
            Q.append((root,1))
            
            while Q:
                node,depth = Q.popleft()
                maxdepth = max(maxdepth,depth)
                if node.left:
                    Q.append((node.left,depth+1))
                if node.right:
                    Q.append((node.right,depth+1))
            
            return maxdepth
        
        return bfs(maxdepth)