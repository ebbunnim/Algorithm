class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> res(2*n,0);
        int idx=0;
        for (int idx=0; idx<n; idx++) {
            res[idx*2] = nums[idx];
            res[idx*2+1] = nums[idx+n];
        }
        return res;
    }
};