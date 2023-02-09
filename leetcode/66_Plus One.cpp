class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> ans = {};
        int carry = 1; // plus 1 starter
        for (int idx=digits.size()-1; idx>=0; idx--) {
            if (digits[idx]+carry==10) {
                ans.push_back(0);
                carry = 1;
            } else {
                ans.push_back(digits[idx]+carry);
                carry = 0;
            }
        }
        if (carry)
            ans.push_back(carry);
        reverse(ans.begin(), ans.end());
        return ans;
    }
};