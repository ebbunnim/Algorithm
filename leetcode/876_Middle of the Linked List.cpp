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
    ListNode* middleNode(ListNode* head) {
        ListNode* currNode = head;
        int nodeLen = 1;
        while (currNode->next) {
            currNode = currNode->next;
            nodeLen++;
        }
        nodeLen = nodeLen/2;

        int idx = 0;
        currNode = head;
        while (idx!=nodeLen) {
            currNode = currNode->next;
            idx++;
        }
        return currNode;
    }
};