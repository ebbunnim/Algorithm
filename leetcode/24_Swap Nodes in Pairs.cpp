/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummy = new ListNode();
        dummy->next = head; 
        ListNode* currNode = dummy;

        while (currNode->next && currNode->next->next) {
            ListNode* preNode = currNode->next;
            ListNode* postNode = currNode->next->next;
            
            preNode->next = postNode->next;
            
            // swap
            currNode->next = postNode; 
            currNode->next->next = preNode; 
            currNode = currNode->next->next;
        }

        return dummy->next;
    }
};