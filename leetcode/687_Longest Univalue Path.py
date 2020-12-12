# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    maxv = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(start):
            if start == None:
                return 0

            left = dfs(start.left)
            right = dfs(start.right)

            if start.left and start.left.val == start.val:
                left += 1
            else:
                left = 0
            if start.right and start.right.val == start.val:
                right += 1
            else:
                right = 0

            # 거리(=>일치하는 개수)
            self.maxv = max(self.maxv, left + right)
            # 상태값
            return max(left, right)

        dfs(root)
        return self.maxv