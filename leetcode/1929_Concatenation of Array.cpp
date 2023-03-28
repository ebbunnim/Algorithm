class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> result(nums.size()*2,0);
        int base = 0;
        while (true) {
            for (int idx=base; idx<nums.size()+base; idx++) {
                result[idx]=nums[idx-base];
            }
            if (base==nums.size()) break;
            base = nums.size();
        }
        return result;
    }
};