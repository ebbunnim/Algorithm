// Solution1 - use string method
class Solution {
public:
    int strStr(string haystack, string needle) {
        return haystack.find(needle);
    }
};

// Solution2 - kmp
class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size();
        int m = needle.size();

        vector<int> pi = getPi(needle, m);
        int j = 0;
        for (int i=0; i < n; i++) {
            while (j > 0 && haystack[i] != needle[j]) {
                j = pi[j-1];
            }
            if (haystack[i] == needle[j]) {
                if (j == m-1) {
                    return i-m+1;
                }
                else
                    j++;
            }
        }   
        return -1;

    }

private: 
    vector<int> getPi(string needle, int m) {
        vector<int> pi(m,0);
        
        int j = 0; 
        for (int i = 1; i < m; i++) {
            while (j > 0 && needle[i] != needle[j]) {
                j = pi[j-1]; // 직전에 일치했던 위치로 back
            }
            if (needle[i] == needle[j]) {
                pi[i] = ++j; // prefix==suffix 일치한 char 개수
            }
        }
        return pi;
    }
};