class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int> target;
        for (int idx=0; idx<nums.size(); idx++) {
            target.insert(target.begin()+index[idx], nums[idx]);
        }
        return target;
    }
};