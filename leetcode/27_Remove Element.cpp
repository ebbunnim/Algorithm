class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int modifiedIdx=0;
        for (int idx=0; idx<nums.size(); idx++) {
            if (nums[idx]!=val) {
                nums[modifiedIdx] = nums[idx];
                modifiedIdx++;
            }
        }
        return modifiedIdx;
    }
};