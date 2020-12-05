# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            # head.next 안건들일 수 있도록 다중할당 사용.단방향 순회 그대로. 근데 포인터 방향은 돌려놔야지
            nex, head.next = head.next, prev 
            prev, head = head, nex # prev set, traverse
        return prev