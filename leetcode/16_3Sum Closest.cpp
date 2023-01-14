class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());

        int ans;
        int middle; 
        int right;
        int threeSum;
        int tmpDiff;
        int diff = INT_MAX;

        for (int left=0; left<nums.size()-2; left++) {
            middle = left+1;
            right = nums.size()-1;
            while (middle<right) {
                threeSum=nums[left]+nums[middle]+nums[right];

                tmpDiff = (target>threeSum) ? abs(target-threeSum) : abs(threeSum-target); // tmpDiff == distance of two nums == (큰수 - 작은수)
                    
                if (tmpDiff==0) 
                    return threeSum;
                
                if (tmpDiff < diff) { // ans && diff 갱신 조건
                    ans = threeSum;
                    diff = tmpDiff;
                }

                if (threeSum > target) { // (주의) abs 값이 아닌 실제 수치로 비교해야 
                    right--;
                } else 
                    middle++;
            }
        }
        return ans;
    }
};