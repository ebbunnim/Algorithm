class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int wealthest(0);
        for (auto account : accounts) {
            int wealth = accumulate(account.begin(), account.end(), 0);
            if (wealthest<wealth) {
                wealthest = wealth;
            }
        }
        return wealthest;
    }
};