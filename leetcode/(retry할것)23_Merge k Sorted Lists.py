import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        root=result=ListNode(None)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))
            
        while heap:
            info = heapq.heappop(heap)
            result.next=info[2]
            result = result.next # traverse
            if result.next:
                heapq.heappush(heap,(result.next.val,info[1],result.next))
        return root.next