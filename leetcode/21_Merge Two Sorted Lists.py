# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# val은 data. root, root.next 는 현재 주소와 다음 주소임.

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode() # head가 가리키는 첫번째 노드로 dummpy 노드를 가리키게 함. 새 노드 추가할 때 첫번째 노드 판별 필요 없음
        head = dummy
        while l1 and l2:
            newnode = ListNode()
            if l1.val<l2.val:
                newnode.val=l1.val
                l1=l1.next
            else:
                newnode.val=l2.val
                l2=l2.next
            dummy.next=newnode
            dummy=dummy.next # traverse
        if l1:
            dummy.next=l1
        if l2:
            dummy.next=l2
        return head.next