// Solution 1
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> uMap;
        for (int idx=0;idx<nums.size();idx++) {
            if (uMap.find(nums[idx])==uMap.end()) 
                uMap[nums[idx]] = 1;
            else 
                return true;
        }
        return false;
    }
};

// Solution 2
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> uSet;
        for (int idx=0;idx<nums.size();idx++) {
            if (uSet.insert(nums[idx]).second==false) // duplicated
                return true;
        }
        return false;
    }
};