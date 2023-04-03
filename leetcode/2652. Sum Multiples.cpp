class Solution {
public:
    int sumOfMultiples(int n) {
        int ans(0);
        for (int num=1; num<=n; num++) {
            if (num%3==0 || num%5==0 || num%7==0) { ans+=num; }
        }
        return ans;
    }
};