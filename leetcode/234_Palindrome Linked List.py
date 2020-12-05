# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        Q = deque()
        while node is not None:
            Q.append(node.val)
            node=node.next
        while len(Q)>=2:
            if Q.popleft()==Q.pop():
                pass
            else:
                return False
        return True