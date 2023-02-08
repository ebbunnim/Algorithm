class Solution {
public:
    vector<int> partial;
    vector<vector<int>> ans;

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        backTracking(0,target,candidates);
        return ans;
    }

    void backTracking(int idx, int target, vector<int>& candidates) {
        // restore ans
        if (target==0) {
            ans.push_back(partial);
            return;
        }
        
        // pruning
        if (target<0 || idx>=candidates.size()) { 
            return;
        }

        // move 
        for (int i=idx; i<candidates.size(); i++) {
            if(i>idx && candidates[i] == candidates[i-1]) // prevent duplicates
                continue;
            partial.push_back(candidates[i]);
            backTracking(i+1, target-candidates[i], candidates);
            partial.pop_back();
        }

    }
    
};