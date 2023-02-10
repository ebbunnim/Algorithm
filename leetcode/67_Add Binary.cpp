class Solution {
public:
    char carry = '0';
    string ans = "";

    string addBinary(string a, string b) {
        int aIdx = a.size()-1;
        int bIdx = b.size()-1;
        char charA;
        char charB;
        while (aIdx>=0 || bIdx>=0) {
            // prevent out of indx
            if (aIdx<0)
                charA='0';
            else 
                charA=a[aIdx];
            if (bIdx<0)
                charB='0';
            else  
                charB = b[bIdx];

            calc(charA, charB);

            --aIdx;
            --bIdx;
        }

        if (carry=='1') 
            ans+='1';

        reverse(ans.begin(),ans.end());

        return ans;

    }

    void calc(char charA, char charB) {
        if (charA=='1' && charB=='1' && carry=='1') {
            ans+='1';
            carry='1';
        } else if (charA=='1' && charB=='1' && carry=='0') {
            ans+='0';
            carry='1';
        } else if (charA=='1' && charB=='0' && carry=='1') {
            ans+='0';
            carry='1';
        } else if (charA=='0' && charB=='1' && carry=='1') {
            ans+='0';
            carry='1';
        } else if (charA=='0' && charB=='0' && carry=='1') {
            ans+='1';
            carry='0';
        } else if (charA=='0' && charB=='1' && carry=='0') {
            ans+='1';
            carry='0';            
        } else if (charA=='1' && charB=='0' && carry=='0') {
            ans+='1';
            carry='0';
        } else {
            ans+='0';
            carry='0';
        }
    }
};