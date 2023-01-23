class Solution1 {
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

class Solution2 {
public:
    int removeDuplicates(vector<int>& nums) {
        int idx = 0; // pointer 1
        for (int num : nums) { // value by pointer 2
            if (!idx || num > nums[idx-1])
                nums[idx++] = num; 
        }
        return idx;
    }
};
