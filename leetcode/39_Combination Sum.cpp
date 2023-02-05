
class Solution {
public:
    vector<vector<int>> ans; 
    vector<int> partial; 

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        backTracking(candidates, 0, target);
        return ans;
    }

    void backTracking(vector<int>& candidates, int currIdx, int target) {
        if (target==0) {
            ans.push_back(partial);
            return; 
        }

        if (target<0 || currIdx==candidates.size()) {// pruning 
            return; 

        partial.push_back(candidates[currIdx]);
        backTracking(candidates, currIdx, target-candidates[currIdx]);
        partial.pop_back();
        backTracking(candidates, ++currIdx, target);
    }
};