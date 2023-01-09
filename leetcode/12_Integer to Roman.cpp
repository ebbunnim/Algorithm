class Solution {
public:
    string intToRoman(int num) {
        string ans = "";
        pair<int, string> values[] = {
            {1000,"M"}, 
            {900,"CM"}, 
            {500,"D"}, 
            {400,"CD"}, 
            {100,"C"}, 
            {90,"XC"}, 
            {50,"L"}, 
            {40,"XL"}, 
            {10,"X"},
            {9,"IX"},
            {5,"V"}, 
            {4,"IV"}, 
            {1,"I"}
        };

        int idx = 0;
        int quotient;
        int remainder;
        while (num>0) {
            if (num < values[idx].first) {
                idx++;
                continue;
            }
            quotient = num/values[idx].first; 
            remainder = num%values[idx].first;
            for (int q=0; q<quotient; q++) {
                ans += values[idx].second;
            }
            num = remainder;
        }
        return ans;
    }
};