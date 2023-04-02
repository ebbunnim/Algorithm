class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> ans;
        for (int idx=0; idx<nums.size(); idx+=2) {
            int freq = nums[idx];
            int val = nums[idx+1];
            for (int fq=0; fq<freq; fq++) {
                ans.push_back(val);
            }
        }
        return ans;
    }
};