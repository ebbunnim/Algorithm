// Solution1
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        if (nums[0]!=0) return 0; // left edge
        int ans = nums.size(); // right edge
        for (int idx=0; idx<nums.size()-1; idx++) {
            if (nums[idx+1]-nums[idx]!=1) {
                ans = nums[idx]+1;
                break;
            }
        }
        return ans;
    }
};

// Solution2
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int total = n*(n+1)/2;
        for (auto num:nums) {
            total-=num;
        }
        return total;
    }
};