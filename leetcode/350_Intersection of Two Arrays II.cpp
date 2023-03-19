class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        int left=0;
        int right=0;
        vector<int> ans;
        
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        while (left<nums1.size() && right<nums2.size()) {
            while (left<nums1.size() && nums1[left]<nums2[right]) 
                left++;
            while (right<nums2.size() && nums1[left]>nums2[right]) 
                right++;
            while (left<nums1.size() && right<nums2.size() && nums1[left]==nums2[right]) {
                ans.push_back(nums1[left]);
                left++;
                right++;
            }
        }
        return ans;
    }
};