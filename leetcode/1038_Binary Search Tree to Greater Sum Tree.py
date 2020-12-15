# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    sumv = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        # 중위순회
        root.right = self.bstToGst(root.right)
        self.sumv+=root.val
        root.val=self.sumv
        root.left = self.bstToGst(root.left)
        return root
