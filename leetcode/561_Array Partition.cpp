class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int ans=0;
        for (int idx=0; idx<nums.size(); idx+=2) {
            ans+=nums[idx];
        }
        return ans;
    }
};