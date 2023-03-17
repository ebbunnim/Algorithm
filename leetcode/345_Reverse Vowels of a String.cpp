class Solution {
public:
    string reverseVowels(string s) {
        int left = 0;
        int right = s.size()-1;
        while (left<right) {
            while (left<s.size() && left<right) {
                if (s[left]==97 || s[left]==101 || s[left]==105 || s[left]==111 || s[left]==117) {
                    left++;
                    break; 
                }
                left++;
            }
            while (right>0 && left<right) {
                if (s[right]==97 || s[right]==101 || s[right]==105 || s[right]==111 || s[right]==117) {
                    right--;
                    break; 
                }
                right--;
            }
            if (left>=right) break;
            int tmp = s[left-1];
            s[left-1] = s[right+1];
            s[right+1] = tmp;
        }
        return s;
    }
};