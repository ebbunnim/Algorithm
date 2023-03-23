class Solution {
public:
    string reverseVowels(string s) {
        int left = 0;
        int right = s.size()-1; 
        bool exit = false;
        while (left < right && left<s.size() && right>=0) {
            while (left<right && left<s.size() && !isVowel(s[left])) {
                left++;
            }
            while (left<right && right>=0 && !isVowel(s[right])) {
                right--;
            }
            char tmpChar = s[left];
            s[left] = s[right];
            s[right] = tmpChar;
            // after processing the vowels
            left++;
            right--;
        }
        return s;
    }
    bool isVowel(char c) {
        if (c==65 || c==69 || c==73 || c==79 || c==85 || c==97 || c==101 || c==105 || c==111 || c==117) 
            return 1;
        return 0;
    }
};