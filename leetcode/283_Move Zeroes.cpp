class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int currIdx = 0;
        for (int idx=0; idx<nums.size(); idx++) {
            if (nums[idx]!=0) {
                nums[currIdx++]=nums[idx];
            }
        }        
        for (currIdx; currIdx<nums.size(); currIdx++) {
            nums[currIdx] = 0;
        }
    }
};