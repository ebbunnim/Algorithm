class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int inplaceIdx = 0; 
        int lastNum = -101; 
        for (int idx=0; idx<nums.size(); idx++) {
            if (nums[idx]>lastNum) {
                lastNum = nums[idx];
                nums[inplaceIdx] = lastNum;
                inplaceIdx++;
            }
        }
        return inplaceIdx;
    }
};