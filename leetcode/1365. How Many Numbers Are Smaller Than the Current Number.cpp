class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> ans;
        int cnt;
        for (int i=0; i<nums.size(); i++) {
            cnt = 0;
            for (int j=0; j<nums.size(); j++) {
                if (i==j) { continue; }
                if (nums[i]>nums[j]) {
                    cnt++;
                }
            }
            ans.push_back(cnt);
        }
        return ans; 
    }
};