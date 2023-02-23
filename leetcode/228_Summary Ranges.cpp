// Solution 1
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        // edge
        if (nums.size()==0)
            return {};
        if (nums.size()==1)
            return {to_string(nums[0])};
        
        vector<string> ans;

        int currNum = nums[0];
        int nxtNum = nums[0];
        for (int idx=1; idx<nums.size(); idx++) {
            if ((long) nums[idx]-nxtNum==1) {
                nxtNum = nums[idx];
            } else {
                if (currNum==nxtNum)
                    ans.push_back(to_string(currNum));
                else 
                    ans.push_back(to_string(currNum)+"->"+to_string(nxtNum));
                currNum = nums[idx];
                nxtNum = nums[idx];
            }
        }
        if (currNum==nxtNum)
            ans.push_back(to_string(currNum));
        else 
            ans.push_back(to_string(currNum)+"->"+to_string(nxtNum));
        return ans;
    }
};

// Solution 2
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ans;
        for (int idx=0; idx<nums.size(); idx++) {
            int pre = nums[idx];
            while (idx+1<nums.size() && (nums[idx+1]==nums[idx]+1)) {
                idx++;
            }
            if (pre==nums[idx])
                ans.push_back(to_string(pre));
            else 
                ans.push_back(to_string(pre)+"->"+to_string(nums[idx]));
        }
        return ans;
    }
};