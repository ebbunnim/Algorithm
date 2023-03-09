/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // 포인터값이 같다면, 동일한 next 노드를 가리키는 것. 
        unordered_set<ListNode*> vis;
        if (headA==headB) return headA;
        while (headA!=NULL) {
            vis.insert(headA);
            headA = headA->next;
        }
        while (headB!=NULL) {
            if (vis.insert(headB).second==false) return headB;
            headB = headB->next;
        }
        return NULL;
    }
};