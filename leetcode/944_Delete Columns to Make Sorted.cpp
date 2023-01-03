class Solution {  
public: 
    int minDeletionSize(vector<string>& strs) {
        int ans = 0; 
        for (int idx=0; idx<strs[0].size(); idx++) {
            for (int num=1; num<strs.size(); num++) {
                if (strs[num-1][idx] > strs[num][idx]) {
                    ans++;
                    break;
                }
            }
        }
        return ans; 
    }
};