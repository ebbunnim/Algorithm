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