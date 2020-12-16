# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    prev = -1e9  # 0으로 하면 1 노드와 만나면 1로 나옴. 가장 작은 수로 할당해야 함.
    minv = 101

    # 중위 순회 + 이전값 저장
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return
        self.minDiffInBST(root.left)

        self.minv = min(self.minv, root.val - self.prev)
        self.prev = root.val

        self.minDiffInBST(root.right)
        return self.minv
