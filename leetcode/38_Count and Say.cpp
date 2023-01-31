class Solution {
public:
    string countAndSay(int n) {
        string res = "";

        while (n--) {
            if (res=="") { // base case
                res = "1";
                continue;
            }
            
            int currCnt = 0; 
            char currChar = res[0];
            string tmpRes = "";
            
            for (int idx=0; idx<res.size(); idx++) {
                if (res[idx]==currChar) {
                    currCnt++; 
                } else {
                    tmpRes += to_string(currCnt);
                    tmpRes += currChar;
                    currChar = res[idx];
                    currCnt = 1; 
                }
            }

            tmpRes += to_string(currCnt);
            tmpRes += currChar;
            res = tmpRes;
        }
        
        return res; 
    }
};
