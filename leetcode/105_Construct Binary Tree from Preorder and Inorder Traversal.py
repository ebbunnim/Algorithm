# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # preorder에서 분할정복에 필요한 값이 순서대로 나오고
        # inorder을 preorder에서 건진 root기준으로 분할 정복하면 됨
        if inorder == []:
            return

        ele = preorder.pop(0)  # 재귀만 아니면 덱으로 변환했을 것
        idx = inorder.index(ele)
        node = TreeNode(inorder[idx])
        node.left = self.buildTree(preorder, inorder[:idx])
        node.right = self.buildTree(preorder, inorder[idx + 1:])
        return node
