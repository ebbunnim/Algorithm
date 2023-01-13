class Solution {
public:
    vector<string> ans; 

    void dfs(int openLeft, int closedLeft, string ansStr) {
        if (openLeft>0) 
            dfs(openLeft-1, closedLeft, ansStr+"(");
        
        if (closedLeft>0 and openLeft<closedLeft)
            dfs(openLeft, closedLeft-1, ansStr+")");
        else if (closedLeft==0) 
            ans.push_back(ansStr);
    
    }

    vector<string> generateParenthesis(int n) {
        dfs(n-1, n, "(");
        return ans;

    }
};