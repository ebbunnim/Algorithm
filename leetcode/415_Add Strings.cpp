class Solution {
public:
    string addStrings(string num1, string num2) {
        int n1 = num1.size()-1;
        int n2 = num2.size()-1;
        int remainder = 0;
        int carry = 0;
        string ans = "";
        int tmpAns = 0;
        while (n1>=0 || n2>=0) {
            if (n1>=0 && n2>=0) {
                tmpAns = ((num1[n1]-'0')+(num2[n2]-'0')+carry)%10;
                carry = ((num1[n1]-'0')+(num2[n2]-'0')+carry)/10;
                n1--;
                n2--;
            } else if (n1>=0) {
                tmpAns = ((num1[n1]-'0')+carry)%10;
                carry = ((num1[n1]-'0')+carry)/10;
                n1--;
            } else if (n2>=0) {
                tmpAns = ((num2[n2]-'0')+carry)%10;
                carry = ((num2[n2]-'0')+carry)/10;
                n2--;
            } 
            ans += to_string(tmpAns);
        }
        if (carry) {
            ans += to_string(carry);
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};