# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = ['#']
        Q = deque([root])
        while Q:
            node = Q.popleft()
            if node:
                Q.append(node.left)
                Q.append(node.right)
                res += [node.val]
            else:
                res += ['#']
        return ' '.join(map(str, res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == "# #": # input=[] 이라고 하면 더미 '#' 담긴 res에서 자식 노드 없으므로 #만 + 되고 큐에 삽입되지 않아 "# #"로 끝남
            return []

        Data = data.split(' ')
        res = TreeNode(val=Data[1])  # root
        Q = deque([res])

        idx = 2
        while Q:
            node = Q.popleft()
            if Data[idx] != '#':
                node.left = TreeNode(val=Data[idx])
                Q.append(node.left)
            idx += 1

            if Data[idx] != '#':
                node.right = TreeNode(val=Data[idx])
                Q.append(node.right)
            idx += 1
        # 참조와 할당을 역할하는 객체가 달리 있음. node에는 left or right 노드로 재할당되는데 res는 그걸 계속 reference로 삼고 있다.
        return res

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))