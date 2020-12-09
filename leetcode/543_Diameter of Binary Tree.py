# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxv=0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):            
            if not root: # left노드 상태값은 -1,-1 자식 노드 가정
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.maxv = max(self.maxv,left+right+2)
            return max(left,right)+1
        
        dfs(root)
        return self.maxv
            