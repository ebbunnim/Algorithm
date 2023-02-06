class Solution {
public:
    int lengthOfLastWord(string s) {
        int sLen = 0; 
        for (int idx=s.size()-1; idx>=0; idx--) {
            if (s[idx]!=' ') {
                sLen++;
                continue;
            }
            if (sLen>0) 
                break;
        }
        return sLen;
    }
};