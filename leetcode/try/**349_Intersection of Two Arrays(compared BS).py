# 특정 값이 존재하지만, 어느 바운더리에 있는지 모르겠다 - 33번 문제 (s<e)
# 이 문제는, 값이 있는지도 모르는 상황.
class Solution:
    #sol1(BS) (53ms)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 한쪽을 정렬하고, nums2에 있는 값을 target으로 이분탐색한다.
        # set 자료형에 넣는다
        def binary_search(l1, x):
            s, e = 0, l1 - 1
            while s <= e:  # 값이 없을 수도 있기 떄문에
                mid = (s + e) // 2
                if nums1[mid] > x:
                    e = mid - 1
                elif nums1[mid] == x:
                    return mid
                else:
                    s = mid + 1
            return -1

        nums1.sort()
        L = len(nums1)
        res = set()
        for n2 in set(nums2):
            if binary_search(L, n2) != -1:
                res.add(n2)
        return res

    # sol2 - easy(40ms)
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     set1 = set(nums1)
    #     set2 = set(nums2)
    #     return set1.intersection(set2)

    # sol3 - two pointers (48ms)
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     # 양쪽 정렬 후 투포인터
    #     nums1.sort()
    #     nums2.sort()
    #     i = j = 0
    #
    #     res = set()
    #     while True:
    #         if i == len(nums1) or j == len(nums2):
    #             break
    #         if nums1[i] < nums2[j]:
    #             i += 1
    #         elif nums1[i] > nums2[j]:
    #             j += 1
    #         else:
    #             res.add(nums1[i])
    #             i += 1
    #             j += 1
    #     return res

