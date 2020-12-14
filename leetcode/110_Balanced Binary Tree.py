# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    flag = 0

    def isBalanced(self, root: TreeNode) -> bool:
        # 상위 노드로 올라가면서 1씩 더해. 근데 val -> left, right 살펴보면서 1이상 차이가 나면 false 리턴
        def dfs(node):
            if self.flag == 1:
                return False
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                self.flag = 1
                return 0
            return max(left, right) + 1

        dfs(root)

        if self.flag == 1:
            return False
        else:
            return True


# solution2
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         def dfs(node):
#             if not node:
#                 return 0
#             left = dfs(node.left)
#             right = dfs(node.right)
#             if left == -1 or right == -1 or abs(left - right) > 1:
#                 return -1
#             return max(left, right) + 1
