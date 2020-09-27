class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        # 두 포인터의 역할 : 서로 중앙으로 오도록 끌어당김
        # 빗물 : left의 max, right의 max에서 각각 현재 height와의 차이를 구한다.
        left_max = right_max = 0
        volume = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:
                volume += (left_max - height[left])
                left += 1
            else:
                volume += (right_max - height[right])
                right -= 1
        return volume

