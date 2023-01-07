class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int ans = (right-left) * min(height[left],height[right]);
        while (left<right) {   
            if (height[left]<height[right]) {
                left++;
            } else {
                right--;
            }
            ans = max(ans, (right-left)*min(height[left],height[right]));
            
        }
        return ans;
    }
};