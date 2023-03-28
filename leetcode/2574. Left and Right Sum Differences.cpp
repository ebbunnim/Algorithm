class Solution {
public:
    vector<int> leftRigthDifference(vector<int>& nums) {
        int n = nums.size();
        vector<int> leftSum(n,0);
        vector<int> rightSum(n,0); 
        vector<int> res;
        for (int idx=1; idx<n; idx++) {
            leftSum[idx] = leftSum[idx-1]+nums[idx-1];
            rightSum[n-1-idx] = rightSum[n-idx]+nums[n-idx];
        }
        for (int idx=0; idx<n; idx++) {
            res.push_back(abs(leftSum[idx]-rightSum[idx]));
        }
        return res;
    }
};