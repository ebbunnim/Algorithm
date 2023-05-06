class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int ans = 0;
        for (int lidx=0; lidx<nums.size(); lidx++) {
            for (int ridx=lidx+1; ridx<nums.size(); ridx++) {
                if (nums[lidx]==nums[ridx]) {
                    ans++;
                }
            }
        }
        return ans;
    }
};