class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n+1,0);
        for (int num=1; num<n+1; num++) {
            ans[num] = (num%2==0) ? ans[num/2] : ans[num/2]+1;
        }
        return ans;
    }
};