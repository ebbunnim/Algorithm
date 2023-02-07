class Solution {
public:
    vector<int> partial;
    set<vector<int>> setAns;

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        backTracking(0,target,candidates);
        vector<vector<int>> ans(setAns.begin(), setAns.end()); 
        return ans;
    }

    void backTracking(int idx, int target, vector<int>& candidates) {
        // restore ans
        if (target==0) {
            setAns.insert(partial);
            return;
        }
        
        // pruning
        if (target<0 || idx>=candidates.size()) { 
            return;
        }

        // move 
        for (int i=idx; i<candidates.size(); i++) {
            partial.push_back(candidates[i]);
            backTracking(++idx, target-candidates[i], candidates);
            partial.pop_back();
        }

    }
    
};