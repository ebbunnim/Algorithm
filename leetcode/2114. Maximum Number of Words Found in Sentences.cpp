class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int maxCnt(0);
        for (auto sentence: sentences) {
            int spaceCnt = count(sentence.begin(), sentence.end(), ' ');
            maxCnt = max(maxCnt, spaceCnt);
        }
        return maxCnt+1;
    }
};