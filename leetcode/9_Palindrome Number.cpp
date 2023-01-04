class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0)
            return false; 
        
        string xString = std::to_string(x);

        bool ans = true; 
        long int left = 0;
        long int right = xString.size()-1;
        
        while (left < right) {
            if (xString[left] != xString[right]) {
                ans = false; 
                break;
            }
            left++;
            right--;
        }
        return ans; 
    }
};