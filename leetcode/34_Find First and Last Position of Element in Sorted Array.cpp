class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int lowerBound = findBound(nums, target);
        int upperBound = findBound(nums, target, true);
        return {lowerBound, upperBound};
    }

private: 
    int findBound(vector<int>& nums, int target, bool upper = false) {
        int bound = -1;
        int start = 0, end = nums.size();
        int mid;
        while (start<end) {
            mid = (start+end)/2;
            if (nums[mid]>target) {
                end = mid; 
            } else if (nums[mid]==target){
                bound = mid;
                if (upper) 
                    start = mid+1; 
                else 
                    end = mid;
            } else {
                start = mid+1;
            }
        }
        return bound;
    }
};