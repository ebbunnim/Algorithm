class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        int mask = 1;
        for (int idx=0; idx<32; idx++) {
            if (n & mask != 0) 
                ans++;
            n >>= 1; 
        }
        return ans;
    }
};