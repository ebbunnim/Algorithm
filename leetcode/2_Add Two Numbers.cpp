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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) { 
        int sumVal; 
        int carry = 0;
        ListNode* dummyHead = new ListNode();
        ListNode* currNode = dummyHead;
        while (l1 || l2) {
            sumVal = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
            carry = sumVal/10; 
            currNode->next = new ListNode(sumVal%10);
            currNode = currNode->next; // [ |]->[ |], [ |]->[ |]->[ |] ... chain을 위한 currNode 
            if (l1)
                l1 = l1->next; 
            if (l2)
                l2 = l2->next; 
        } 
        if (carry)
            currNode->next = new ListNode(carry);
        return dummyHead->next;
    }
};
