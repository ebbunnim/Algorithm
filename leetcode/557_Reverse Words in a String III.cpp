class Solution {
public:
    string reverseWords(string s) {
        int sIdx=0;
        for (int idx=0; idx<s.size(); idx++) {
            if (s[idx]==' ') {
                reverse(s.begin()+sIdx, s.begin()+idx);
                sIdx=idx+1;
            }
        }
        if (sIdx<s.size()) {
            reverse(s.begin()+sIdx, s.end());
        }
        return s;
    }
};