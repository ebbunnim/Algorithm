class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        unordered_set<int> uset{nums.begin(), nums.end()};
        vector<int> ans;
        for (int idx=1; idx<=nums.size(); idx++) {
            if (uset.find(idx)==uset.end()) {
                ans.push_back(idx);
            }
        }
        return ans;
    }
};