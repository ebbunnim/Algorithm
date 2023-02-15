class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int,int> uMap;
        unordered_set<int> uSet;
        for (int idx=0;idx<nums.size();idx++) {
            if (uMap.find(nums[idx])!=uMap.end()) {
                if (abs(uMap[nums[idx]]-idx)<=k)
                    return true;
                else 
                    uMap[nums[idx]] = idx; // replace key
            } else {
                uMap[nums[idx]] = idx; // first key set
            }
        }   
        return false;
    }  
};