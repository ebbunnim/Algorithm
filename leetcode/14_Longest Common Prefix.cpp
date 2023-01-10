class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        
        sort(strs.begin(), strs.end());
        string ans = ""; 
        
        string str1 = strs[0]; 
        string str2 = strs[n-1]; 
        
        for(int i = 0; i < str1.length(); i++){
            if(str1[i] == str2[i]){
                ans += str1[i];
            }else{
                break;
            }
        }
        return ans;
    }
};