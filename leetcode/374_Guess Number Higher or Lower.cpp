/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int s=1;
        int e=n;
        while (s<e) {
            int mid = s+(e-s)/2;
            int apiRet = guess(mid);
            if (apiRet==-1) {
                e = mid; // Q. e = mid-1, s = mid 가 되면 안되는 이유?
            } else if (apiRet==1) {
                s = mid+1;
            } else {
                return mid;
            }
        }
        return 1;
    }
};