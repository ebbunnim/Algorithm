class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int ans(0);
        for (int num : nums) {
            ans += num; 

            int remainder;
            int quotient = num;
            while (quotient>0) {
                remainder = quotient%10;
                quotient = quotient/10; 
                ans -= remainder;
            }
        }
        return ans; 
    }
};