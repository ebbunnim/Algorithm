class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int lastSum(0);
        for (int idx=0; idx<nums.size(); idx++) {
            nums[idx] += lastSum;
            lastSum = nums[idx];
        }
        return nums;
    }
};