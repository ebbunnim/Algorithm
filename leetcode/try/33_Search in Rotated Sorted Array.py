class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot : min값을 찾는다.
        # pivot값 기준으로 인덱싱하고 target 값을 찾아야 한다.
        s, e = 0, len(nums) - 1
        while s < e:  # 내가 임의적으로 검색 범위를 두 집단으로 남았기 때문에, pivot 위치가 ==일때는 그 중 어디에 속하는지 지정해야. 여기서는 s<e로 설정해야 하는 것 주의
            mid = (s + e) // 2  # pivot이 위치한 인덱스 찾기
            if nums[mid] > nums[e]:
                s = mid + 1
            else:
                e = mid
        pivot = e

        # target 위치 찾기
        s, e = 0, len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            mid_pivot = (pivot + mid) % len(nums)  # 회전되어 있으므로, 피벗을 기준으로 인덱싱 되어야 한다.
            if nums[mid_pivot] < target:
                s = mid + 1
            elif nums[mid_pivot] > target:
                e = mid - 1
            else:
                return mid_pivot
        return -1

