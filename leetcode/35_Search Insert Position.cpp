class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size();
        int mid;
        while (start<end) {
            mid = (start+end)/2;
            if (nums[mid]>target) 
                end = mid;
            else if (nums[mid]==target)
                return mid; 
            else 
                start = mid+1;
        }
        return start;
    }
};