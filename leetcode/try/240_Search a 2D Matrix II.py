class Solution:
    def searchMatrix(self, matrix, target):
        # 대빵나와..!
        # 대빵보다 작으면, 왼쪽으로 순회해서 찾아, 없으면 다음 행
        # 만약, 대빵보다 크면 다음 행에서 왼쪽으로 순회해서 찾아
        if matrix == [[]]:
            return False

        for i in range(len(matrix)):
            if target < matrix[i][-1]:
                s, e = 0, len(matrix[0]) - 1
                while s <= e:
                    mid = (s + e) // 2
                    if matrix[i][mid] < target:
                        s = mid + 1
                    elif matrix[i][mid] == target:
                        return True
                    else:
                        e = mid - 1
            elif target == matrix[i][-1]:  # [[-5]] -5 : 항상 반례는 원소 없을때, 양쪽 끝단에 있을 때를 확인해야
                return True
            else:
                continue
        return False

    # sol2 - pythonic
    # return any(target in row for row in matrix)





