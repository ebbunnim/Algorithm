class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n==0) return false;

        int remainder;
        while (true) {
            if (n==0 || n==1) // n : qutient 
                return true;
            remainder = n%2;
            if (remainder != 0)
                break;
            n /= 2; 
        }
        return false;
    }
};