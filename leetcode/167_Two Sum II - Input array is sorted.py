# 이 문제, 투포인터로 풀되 연속된 부분합 아님을 명시
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers.sort() # already sorted
        s, e = 0, len(numbers) - 1  # 값을 감소시키는, 값을 증가시키는 애
        sumv = 0
        flag = 0
        while s < e:
            sumv = numbers[s] + numbers[e]
            if sumv > target:
                e -= 1
            elif sumv == target:
                return [s + 1, e + 1]
            else:
                s += 1
    #sol2 - BS
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     for idx, val in enumerate(numbers):  # 한 원소 고정
    #         s, e = idx + 1, len(numbers) - 1  # idx+1부터 순회해야 [2,3,4] 6  중복값 처리
    #         _target = target - val
    #         ans1 = ans2 = 1001
    #         while s <= e:  # 다른 원소 찾으러 갑니다
    #             mid = (s + e) // 2
    #             if numbers[mid] > _target:
    #                 e = mid - 1
    #             elif numbers[mid] == _target:
    #                 return [idx + 1, mid + 1]
    #             else:
    #                 s = mid + 1
