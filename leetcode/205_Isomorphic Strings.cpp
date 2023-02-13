class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> sUmap;
        unordered_map<char, char> tUmap;
        for (int idx=0; idx<s.size(); idx++) {
            if (sUmap.find(s[idx]) == sUmap.end() && tUmap.find(t[idx]) == tUmap.end()) { // 둘다 없다.
                sUmap[s[idx]] = t[idx];
                tUmap[t[idx]] = s[idx];
            } else if ( sUmap.find(s[idx]) != sUmap.end() && tUmap.find(t[idx]) != tUmap.end() ) { 
                if (sUmap[s[idx]]!=t[idx] || tUmap[t[idx]]!=s[idx]) 
                    return false;
            } else {
                return false;
            }
        }
        return true;

    }
};