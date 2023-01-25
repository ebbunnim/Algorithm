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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* leftNode = head; 
        ListNode* rightNode = head; 

        for (int idx=0; idx<n; idx++) {
            rightNode = rightNode->next; 
        }

        if (!rightNode) { // n == sz
            return head->next;
        }

        while (rightNode->next) {
            rightNode = rightNode->next;
            leftNode = leftNode->next; 
        }
        
        leftNode->next = leftNode->next->next;
        return head;
    }
};