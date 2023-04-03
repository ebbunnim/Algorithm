class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string ans=s;
        for (int idx=0; idx<s.size(); idx++) {
            ans[indices[idx]] = s[idx];
        }
        return ans;
    }
};