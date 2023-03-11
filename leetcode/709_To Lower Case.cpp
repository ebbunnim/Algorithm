class Solution {
public:
    string toLowerCase(string s) {
        for (int idx=0; idx<s.size(); idx++) { 
            if (s[idx]>='A' and s[idx]<='Z') {
                s[idx] = s[idx]+32;
            }
        }
        return s;
    }
};