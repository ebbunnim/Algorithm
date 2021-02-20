class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 양쪽 정렬 후 투포인터
        nums1.sort()
        nums2.sort()
        i = j = 0

        res = set()
        while True:
            if i == len(nums1) or j == len(nums2):
                break

            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.add(nums1[i])
                i += 1
                j += 1
        return res
