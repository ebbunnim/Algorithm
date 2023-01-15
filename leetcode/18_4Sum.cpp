class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        
        sort(nums.begin(), nums.end());;

        int left;
        int right;
        long fourSum;
        int numsLength = nums.size();

        // (주의) left 포인터를 총합++, right 포인터를 총합-- 로 활용하고 싶다면, static pointer들은 붙어있어야 한다.
        for (int staticLeft=0; staticLeft<numsLength-3; staticLeft++) {
            if (staticLeft>0 && nums[staticLeft]==nums[staticLeft-1]) continue;
            for (int staticRight=staticLeft+1; staticRight<numsLength-2; staticRight++) {
                if (staticRight>staticLeft+1 && nums[staticRight]==nums[staticRight-1]) continue;

                left = staticRight+1;
                right = numsLength-1;

                while (left<right) {
                    fourSum = (long) nums[staticLeft] + nums[staticRight] + nums[left] + nums[right];
                    if (fourSum==target) {
                        ans.push_back({nums[staticLeft],nums[left],nums[right],nums[staticRight]});
                        while (left<right && nums[left]==nums[left+1]) 
                            left++;
                        while (left<right && nums[right]==nums[right-1]) 
                            right--;
                        left++;
                        right--;
                    } else if (fourSum<target) { 
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        return ans;
    }
};