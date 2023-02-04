// Intuition : x^n = x^(2*(n/2)) if n%2==0
class Solution {
public:
    double myPow(double x, int n) {
        if (n==0) 
            return 1; // base case
        if (n==INT_MIN) { // edge. If n equals INT_MIN, -n cannot be represented in type 'int'
            x = 1/x;
            return myPow(x*x, -(n/2)); 
        }
        if (n<0) {
            n = -n; 
            x = 1/x;
        }
        return n%2==0 ? myPow(x*x, n/2) : x*myPow(x*x, n/2);
    }
};