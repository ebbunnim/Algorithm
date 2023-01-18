class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) { 
        // Q. 아래 두 줄의 의미. 왜 dummy만 생성하면 안되는지? Q. ListNode dummy; ListNode* currNode = &dummy; 와 같은 의미인지 확인
        ListNode* dummy = new ListNode(); 
        ListNode* currNode = dummy; 
        int addResult;
        int carry = 0;
        while (l1 || l2) {
            addResult = carry + (l1? l1->val : 0) + (l2 ? l2->val : 0); // Q. carry까지 더하는 이유?
            carry = addResult/10; 
            currNode->next = new ListNode((addResult%10));
            currNode = currNode->next; 
            if (l1) 
                l1 = l1->next; 
            if (l2) 
                l2 = l2->next; 
        }
        if (carry)
            currNode->next = new ListNode(carry);
        return dummy->next; // Q. dummy.next vs dummy->next
}};
