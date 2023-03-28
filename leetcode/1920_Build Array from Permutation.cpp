class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> ans(nums.size(), 0);
        for (int idx=0; idx<nums.size(); idx++) {
            ans[idx] = nums[nums[idx]];
        }
        return ans;
    }
};