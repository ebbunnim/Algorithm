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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* currNode = head;
        while (currNode && currNode->next) {
            if (currNode->next->val==val) {
                currNode->next = currNode->next->next;
            } else {
                currNode = currNode->next;
            }
        }
        // edge (start node value equals val)
        if (head && head->val==val) {
            head = head->next;
        }
        return head;
    }
};