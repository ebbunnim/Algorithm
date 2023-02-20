// Solution 1
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

// Solution 2 - refactor
class Solution {
public:
    int addDigits(int num) {
        long currSum = 0;
        while (num>9) {
            while (num>0) {
                currSum += (num%10);
                num /= 10;
            }
            // reset 
            num = currSum;
            currSum = 0;
        }
        return num;
    }
};
