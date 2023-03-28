class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        for (string op: operations) {
            if (op.front()=='+' || op.back()=='+')
                x++;
            else 
                x--;
        }
        return x;
    }
};