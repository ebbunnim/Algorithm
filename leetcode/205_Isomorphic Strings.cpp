// Solution 1
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> sUmap;
        unordered_map<char, char> tUmap;
        for (int idx=0; idx<s.size(); idx++) {
            if (sUmap.find(s[idx]) == sUmap.end() && tUmap.find(t[idx]) == tUmap.end()) { // key absent (all umap)
                sUmap[s[idx]] = t[idx];
                tUmap[t[idx]] = s[idx];
            } else if ( sUmap.find(s[idx]) != sUmap.end() && tUmap.find(t[idx]) != tUmap.end() ) { // key exists (all umap)
                if (sUmap[s[idx]]!=t[idx] || tUmap[t[idx]]!=s[idx]) 
                    return false;
            } else {
                return false;
            }
        }
        return true;

    }
};

// Solution 2
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> sUmap;
        unordered_map<char, char> tUmap;
        for (int idx=0; idx<s.size(); idx++) {
            if (sUmap[s[idx]] && sUmap[s[idx]]!=t[idx]) return false;
            if (tUmap[t[idx]] && tUmap[t[idx]]!=s[idx]) return false;
            sUmap[s[idx]]=t[idx];
            tUmap[t[idx]]=s[idx];
        }
        return true;

    }
};