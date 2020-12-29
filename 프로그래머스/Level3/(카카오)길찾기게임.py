import sys
sys.setrecursionlimit(10 ** 9)

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def solution(nodeinfo):
    for idx, val in enumerate(nodeinfo):
        nodeinfo[idx] = [idx + 1, val]
    nodeinfo.sort(key=lambda x: (-x[1][1], x[1][0]))  # y큰,x작 기준으로 정렬

    def add(root, nxt):
        if nxt[1][0] < root.val[1][0]:
            if root.left == None:
                root.left = TreeNode(val=nxt)
            else:
                add(root.left, nxt)
        else:
            if root.right == None:
                root.right = TreeNode(val=nxt)
            else:
                add(root.right, nxt)

    def preorder(pre, node):
        if not node
            return
        pre += [node.val[0]]
        preorder(pre, node.left)
        preorder(pre, node.right)
        return pre

    def postorder(post, node):
        if not node:
            return
        postorder(post, node.left)
        postorder(post, node.right)
        post += [node.val[0]]
        return post

    root = TreeNode()
    root.val = nodeinfo[0]

    for nxt in nodeinfo[1:]:
        add(root, nxt)

    return ([preorder([], root), postorder([], root)])

