class Solution {
public:
    int countSegments(string s) {
        int ans = 0;
        int findAlpha = false;
        for (int idx=0; idx<s.size(); idx++) {
            if (s[idx]!=' ') {
                findAlpha = true;
            } else {
                if (findAlpha) {
                    ans++;
                    findAlpha = false;
                }
            }
        }
        if (findAlpha) 
            ans++;
        return ans;
    }
}; 