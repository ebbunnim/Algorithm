// 요구사항: 합쳐서 target이 되는 두 수의 index를 반환해라 
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashMap; 
        
        for (int idx = 0; idx < nums.size(); idx++) {
            int diff = target - nums[idx]; 
            if ( hashMap.find(diff) != hashMap.end() ) {
                return {idx, hashMap[diff]};
            } else {
                hashMap[nums[idx]] = idx;
            }
        }
        return {};
    }
};