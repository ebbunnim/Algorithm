class Solution {
public:
    int addDigits(int num) {
        int currDigit;
        long currSum = 0;
        while (true) {
            while (num>0) {
                currDigit = num % 10;
                num /= 10;
                currSum += currDigit;
            }
            if (isOneDigit(currSum))
                return currSum;
            
            // reset 
            num = currSum;
            currSum = 0;
        }

    }
    bool isOneDigit(int number) {
        return number/10==0 ? true : false;
    }
};