/*
    Intuition: [ x -> quotient / remainder 활용. 연산 횟수 늘어날수록 quotient는 자릿수 올리기 ]
    123 -> 12 / 3 
    12 -> 1 / 2
    1 -> 0 / 1  (quotient 0일때 exit)
*/
class Solution {
public:
    int reverse(int x) {
        long ans = 0; 
        int remainder; 
        while (x) {
            remainder = x%10;
            ans = (ans*10) + remainder;
            if (ans>INT_MAX) return 0; 
            if (ans<INT_MIN) return 0; 
            x /= 10; 
        } 
        return (long) ans; 
    }
};