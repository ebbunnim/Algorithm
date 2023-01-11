class Solution {
public:
    int romanToInt(string s) {
        unordered_map<string, int> hashMap; 
        hashMap["I"] = 1; 
        hashMap["V"] = 5;
        hashMap["X"] = 10;
        hashMap["L"] = 50;
        hashMap["C"] = 100;
        hashMap["D"] = 500;
        hashMap["M"] = 1000;
        hashMap["IV"] = 4;
        hashMap["IX"] = 9;
        hashMap["XL"] = 40;
        hashMap["XC"] = 90;
        hashMap["CD"] = 400;
        hashMap["CM"] = 900;

        int ans = 0;

        string curr_char;
        string pre_char="z";
        int curr_num;
        int pre_num = 4000; 

        for (int idx=0; idx<s.size(); idx++) {
            curr_char = s.at(idx);
            curr_num = hashMap[curr_char];
            if (curr_num > pre_num) {
                ans -= pre_num;
                ans += hashMap[pre_char+curr_char];
            } else { 
                ans += curr_num;
            }
            pre_char = curr_char;
            pre_num = curr_num;
        }
        return ans;
        
    }
};