class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int idx1 = m-1;
        int idx2 = n-1;
        int currIdx = m+n-1;
        while (idx1>=0 and idx2>=0){
            if (nums2[idx2]>=nums1[idx1]) 
                nums1[currIdx--] = nums2[idx2--];
            else
                nums1[currIdx--] = nums1[idx1--];
        }
        while (idx2>=0) {
            nums1[currIdx--] = nums2[idx2--];
        }
    }
};

/* NOTE
: intuition은 three pointers
: O(n*m) -> O(n+m) 이 핵심
: non-decreasing order를 활용하는 것이 중요
: ex. [1,2,3,0,0,0], [2,5,6] 에서 3,6을 비교. 6이 더 크다면 [1,2,3,0,0,6] 으로 가장 끝 인덱스에 배치. 이후 3,5 비교 후 배치 etc 반복
: [1,2,3,0,0,6] -> [1,2,3,0,5,6] -> [1,2,3,3,5,6] -> [1,2,2,3,5,6]
: two array 순회 방향은 right -> left
: 현재 가장 큰 인덱스는 currIdx로 표현. In move, currIdx--
*/