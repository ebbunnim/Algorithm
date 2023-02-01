class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<set<char>> row(9), col(9), box(9);

        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                char val = board[i][j];
                if (val=='.') 
                    continue;
                if (!row[j].insert(val).second || !col[i].insert(val).second || !box[(i/3)*3+j/3].insert(val).second) { // check repetition occured
                    return false;
                }
                
            }
        }
        return true;
    }
};