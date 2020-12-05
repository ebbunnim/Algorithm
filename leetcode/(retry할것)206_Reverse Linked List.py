# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            # 현재의 head.next 안건들일 수 있도록 다중할당 사용. 단방향 순회 그대로이지만 포인터 방향은 반대로 돌려놓은 상태
            nex, head.next = head.next, prev 
            prev, head = head, nex # prev set, traverse
        return prev