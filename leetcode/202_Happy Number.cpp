class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> visited;
        int remainder = 0;
        long tmpRes; 
        while (true) {
            tmpRes = 0;
            while (n!=0) {
                remainder = n%10;
                n /=10;
                tmpRes += pow(remainder,2);
            }
            if (tmpRes==1) return true;
            if (visited.insert(tmpRes).second==false) return false;
            n = tmpRes;
        }
    }
};